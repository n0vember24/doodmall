from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from parler.admin import TranslatableAdmin

from users.models import User, Order, Cart, Notification


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        (None, {"fields": ("phone_number", "username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "phone_number", "last_name", "email")
    ordering = ("first_name",)
    readonly_fields = ('date_joined', 'last_login', 'is_staff', 'is_superuser', 'user_permissions')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = list_filter = search_fields = ordering = ('user', 'order_time')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'products_count')
    list_filter = search_fields = ordering = ('user',)
    readonly_fields = ('user', 'products')


@admin.register(Notification)
class NotificationAdmin(TranslatableAdmin):
    readonly_fields = ('user',)


# class GroupMeta:
#     app_label = User._meta.app_label
#
#
admin.site.unregister(Group)
# group_model = type("Group", (Group,), {'__module__': '', 'Meta': GroupMeta})
# admin.site.register(group_model, GroupAdmin)
