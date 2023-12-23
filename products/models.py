from django.core.validators import MinLengthValidator, FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db.models import Model, CharField, TextField, ImageField, SlugField, ForeignKey, SET_NULL, DateField, \
    CASCADE, BooleanField, DateTimeField, PositiveSmallIntegerField
from django.utils.translation import gettext_lazy as _


class Country(Model):
    name = CharField(
        _('Name of Country'),
        max_length=30,
        validators=(MinLengthValidator(3),)
    )
    slug = SlugField(max_length=40, unique=True)


class Brand(Model):
    title = CharField(
        _('Title of brand'),
        max_length=30,
        help_text=_("Required. The title must consist minimum 2 and maximum 30 characters."),
        validators=[MinLengthValidator(2)]
    )
    about = TextField(
        _('Description of the brand'),
        max_length=500,
        null=True,
        blank=True,
        help_text=_('Not required. The description must consist minimum 50 and maximum 500 characters.'),
    )
    logo = ImageField(
        _('Logo of the brand'),
        upload_to='brands/logos/',
        validators=(FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg')),)
    )
    country = ForeignKey('products.Country', SET_NULL, null=True)
    found_year = DateField(_('Year of brand foundation'), null=True, blank=True)


class Category(Model):
    title = CharField(
        _('Title of Category'),
        max_length=50,
        validators=(MinLengthValidator(2),)
    )
    about = TextField(
        max_length=250,
        null=True,
        blank=True,
        help_text=_('Not required. The description must consist minimum 25 and maximum 250 characters.'),
    )
    slug = SlugField(max_length=60, unique=True)


class SubCategory(Model):
    parent = ForeignKey('products.Category', SET_NULL, null=True)
    title = CharField(
        _('Title of Subcategory'),
        max_length=50,
        validators=(MinLengthValidator(2),)
    )
    slug = SlugField(max_length=60, unique=True)


class Product(Model):
    title = CharField(
        _('Title of Product'),
        max_length=200,
        validators=(MinLengthValidator(5),)
    )
    slug = SlugField(max_length=200, validators=(MinLengthValidator(5),))
    category = ForeignKey('products.SubCategory', SET_NULL, null=True)
    is_exists = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    count = PositiveSmallIntegerField(
        _('Count of products'),
        default=1,
    )

    def save(self, *args, **kwargs):
        if self.count == 0:
            self.is_exists = False
        return super().save(*args, **kwargs)


class Review(Model):
    user = ForeignKey('users.User', SET_NULL, null=True)
    product = ForeignKey('products.Product', CASCADE)
    score = PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'product')
