from django.core.validators import MinLengthValidator, FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db.models import Model, CharField, TextField, ImageField, SlugField, ForeignKey, SET_NULL, DateField, \
    CASCADE, BooleanField, DateTimeField, PositiveSmallIntegerField, JSONField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Country(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(
            _('Name of Country'),
            max_length=30,
            validators=(MinLengthValidator(3),)
        )
    )
    slug = SlugField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class Brand(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(
            _('Title of brand'),
            max_length=30,
            help_text=_("Required. The title must consist minimum 2 and maximum 30 characters."),
            validators=[MinLengthValidator(2)]
        ),
        about=TextField(
            _('Description of the brand'),
            max_length=500,
            null=True,
            blank=True,
            help_text=_('Not required. The description must consist minimum 50 and maximum 500 characters.'),
        )
    )
    logo = ImageField(
        _('Logo of the brand'),
        upload_to='brands/logos/',
        validators=(FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg')),)
    )
    country = ForeignKey('products.Country', SET_NULL, null=True)
    found_year = DateField(_('Year of brand foundation'), null=True, blank=True)

    def __str__(self):
        return self.title


class Category(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(
            _('Title of Category'),
            max_length=50,
            validators=(MinLengthValidator(2),)
        ),
        about=TextField(
            max_length=250,
            null=True,
            blank=True,
            help_text=_('Not required. The description must consist minimum 25 and maximum 250 characters.'),
        )
    )
    slug = SlugField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class SubCategory(TranslatableModel):
    parent = ForeignKey('products.Category', SET_NULL, null=True)
    translations = TranslatedFields(
        title=CharField(
            _('Title of Subcategory'),
            max_length=50,
            validators=(MinLengthValidator(2),)
        )
    )
    slug = SlugField(max_length=60, unique=True)

    class Meta:
        verbose_name = _('Sub Category')
        verbose_name_plural = _('Sub Categories')

    def __str__(self):
        return self.title


class Product(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(
            _('Title of Product'),
            max_length=200,
            validators=(MinLengthValidator(5),)
        ),
        description=CharField(
            _('Description of product'),
            max_length=255,
            null=True,
            blank=True
        )
    )

    slug = SlugField(max_length=200, validators=(MinLengthValidator(5),))
    attrs = JSONField(default=dict)
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

    def __str__(self):
        return self.title


class ProductImage(Model):
    product = ForeignKey('products.Product', SET_NULL, null=True)
    image = ImageField(upload_to='products/images/')


class Review(Model):
    user = ForeignKey('users.User', SET_NULL, null=True)
    product = ForeignKey('products.Product', CASCADE)
    score = PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'product')
