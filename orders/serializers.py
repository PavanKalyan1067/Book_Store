from rest_framework import serializers

from .models import Order, Status


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'book',
            'book_quantity',
            'address',
            'status',
        ]
        read_only_fields = ['id', 'status']

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
    user_id = serializers.IntegerField()
    book_id = serializers.IntegerField()
    book_quantity = serializers.IntegerField()
    total_price = serializers.FloatField()
    address = serializers.CharField()

    class Meta:
        model = Order
        fields = [
            'user_id',
            'book_id',
            'book_quantity',
            'total_price',
            'address'
        ]
