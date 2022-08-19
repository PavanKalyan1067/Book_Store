from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'book',
            'book_quantity',
            'user',
            'address'
        ]

    def create(self, validated_data):
        book = validated_data.get('book')
        book_quantity = validated_data.get('book_quantity')
        if book.book_quantity < book_quantity:
            raise Exception('book out of stock')
        book.book_quantity -= book_quantity
        book.save()
        total_price = book.price * book_quantity
        validated_data.update({'total_price': total_price})
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
