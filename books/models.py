from django.db import models
from accounts.models import User


class Book(models.Model):
    book_title = models.CharField(max_length=50, unique=True, blank=False)
    author = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField(max_length=100)
    book_quantity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title


