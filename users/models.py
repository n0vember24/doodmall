from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MinLengthValidator
from django.db.models import Model, CharField, ForeignKey, ManyToManyField, DateTimeField, OneToOneField, \
    CASCADE, BooleanField, TextField, SET_NULL
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from users.validators import PhoneNumberValidator


class User(AbstractUser):
    phone_number_validator = PhoneNumberValidator()
    phone_number = CharField(
        _('phone number'),
        max_length=9,
        unique=True,
        help_text=_("Required. The phone number must consist of 9 digits and start."),
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
        validators=(phone_number_validator,),
    )

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
        swappable = "AUTH_USER_MODEL"


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
    user = ForeignKey('users.User', CASCADE)
    is_read = BooleanField(_('Is read'), default=False)
    time = DateTimeField(
        _("Received date and time"),
        auto_now_add=True
    )

    def __str__(self):
        return self.translations.title
