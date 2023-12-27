from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
