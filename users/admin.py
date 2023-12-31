from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from users.models import User, Order, Cart, Notification


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass


# class GroupMeta:
#     app_label = User._meta.app_label
#
#
admin.site.unregister(Group)
# group_model = type("Group", (Group,), {'__module__': '', 'Meta': GroupMeta})
# admin.site.register(group_model, GroupAdmin)
