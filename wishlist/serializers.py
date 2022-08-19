from rest_framework import serializers

from orders.models import Order


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'book',
            'book_quantity',
            'user',
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


class GetWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
