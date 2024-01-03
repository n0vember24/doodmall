from django.apps import apps
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinLengthValidator
from django.db.models import Model, CharField, ForeignKey, ManyToManyField, DateTimeField, OneToOneField, \
    CASCADE, BooleanField, TextField, SET_NULL
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from users.validators import PhoneNumberValidator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone number must be set")
        # email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)

    def with_perm(
            self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractUser):
    phone_number_validator = PhoneNumberValidator()
    username_validator = UnicodeUsernameValidator()

    phone_number = CharField(
        _('phone number'),
        max_length=9,
        unique=True,
        help_text=_(
            "Required. The phone number must consist of 9 digits and start without region code. Example: 944444444"),
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
        validators=(phone_number_validator,),
    )

    username = CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    first_name = CharField(_("first name"), max_length=150)

    objects = UserManager()

    REQUIRED_FIELDS = ('first_name',)
    USERNAME_FIELD = 'phone_number'

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return '%s(%s)' % (self.first_name, self.phone_number)


class Order(Model):
    user = ForeignKey('users.User', SET_NULL, null=True)
    product = ManyToManyField('products.Product')
    order_time = DateTimeField(
        _('Order time'),
        auto_now_add=True
    )

    def __str__(self):
        return '%s: %s' % (self.id, self.user.first_name)


class Cart(Model):
    user = OneToOneField('users.User', CASCADE, primary_key=True, unique=True)
    products = ManyToManyField('products.Product')

    def products_count(self):
        return self.products.count()

    products_count.short_description = _('Products Count')
    products_count.allow_tags = True

    def __str__(self):
        return self.user.first_name


class Notification(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(
            _('Title'),
            max_length=70,
            help_text=_('Required. The title must consist minimum 2 characters and maximum 70.'),
            validators=(MinLengthValidator(2),)
        ),
        message=TextField(
            _('Message of notification'),
            max_length=500,
            help_text=_('Required. The text must consist minimum 20 characters and maximum 500'),
            validators=(MinLengthValidator(20),)
        )
    )
    user = ManyToManyField('users.User')
    is_read = BooleanField(_('Is read'), default=False)
    time = DateTimeField(
        _("Received date and time"),
        auto_now_add=True
    )

    def __str__(self):
        return self.translations.title
