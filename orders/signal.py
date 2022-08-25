from django.db.models.signals import pre_save
from django.dispatch import receiver

from orders.models import Order


@receiver(pre_save, sender=Order)
def create_order(sender, instance, **kwargs):
    if instance.book.book_quantity < instance.book_quantity:
        raise Exception('book out of stock')
    instance.book.book_quantity = int(instance.book.book_quantity) - int(instance.book_quantity)
    instance.book.save()
    instance.total_price = int(instance.book.price) * int(instance.book_quantity)
