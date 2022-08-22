from rest_framework import serializers

from .models import Order, Status


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
            'address',
            'status',
            'user',
        ]
        read_only_fields = ['id', 'status', 'user', 'address']

    def create(self, validated_data):
        book = validated_data.get('book')
        book_quantity = validated_data.get('book_quantity')
        if book.book_quantity < book_quantity:
            raise Exception('book out of stock')
        book.book_quantity -= book_quantity
        book.save()
        total_price = book.price * book_quantity
        validated_data.update({'total_price': total_price})
        validated_data['status'] = Status.OR
        return self.Meta.model.objects.create(**validated_data)


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
