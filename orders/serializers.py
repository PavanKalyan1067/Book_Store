from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    def get_address(self, obj):
        return obj.user.address

    class Meta:
        model = Order
        fields = [
            'id',
            'book',
            'book_quantity',
            'total_price',
            'address',
            'status',
            'user',
        ]
        read_only_fields = ['id', 'status', 'user', 'address', 'total_price',
]


class GetOrderSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    def get_address(self, obj):
        return obj.user.address

    class Meta:
        model = Order

        fields = [
            'id',
            'user',
            'book_id',
            'book_quantity',
            'total_price',
            'status',
            'address',
        ]
        read_only_fields = ['id', 'status']
