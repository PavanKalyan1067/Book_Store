from rest_framework import serializers

from orders.models import Order


class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'book',
            'book_quantity',
            'status',
        ]
        read_only_fields = ['id', 'status']


class GetAllCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
