from rest_framework.serializers import ModelSerializer

from users.models import User, Order, Cart, Notification


class UserSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class OrderSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Order


class CartSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cart


class NotificationSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Notification
