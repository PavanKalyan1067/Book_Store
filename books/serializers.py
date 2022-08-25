from rest_framework import serializers
from books.models import Book


class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'book_title',
            'author',
            'price',
            'description',
            'book_quantity'
        ]
        required_field = [
            'book_title',
            'author',
            'price',
            'book_quantity'
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'book_title',
            'author',
            'price',
            'book_quantity',
            'description',
        ]
