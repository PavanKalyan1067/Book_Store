from django.conf import settings
from django.db import models

from books.models import Book


class Status(models.TextChoices):
    CA = 'CART'
    OR = 'ORDER'
    WL = 'WISHLIST'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    book_quantity = models.IntegerField(null=False)
    total_price = models.IntegerField(null=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status.choices, default=Status.CA, max_length=10)

    def order(self):
        return {
            'user': self.user.id,
            'book': self.book.id,
            'book_quantity': self.book_quantity,
            'total_price': self.total_price,
            'status': self.status,
            'date_ordered': self.date_ordered,

        }