from rest_framework import serializers

from orders.models import Order


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'book',
            'book_quantity',
            'status',
        ]


class GetWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
