from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.core.signals import request_finished
from orders.models import Order
from django.dispatch import receiver, Signal


@receiver(pre_save, sender=Order)
def create_order(sender, instance, **kwargs):
    print('order created')


@receiver(post_save, sender=Order)
def update_order(sender, instance, **kwargs):
    print('order updated')


@receiver(post_delete, sender=Order)
def delete_order(sender, instance, **kwargs):
    print('order deleted')


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


abd = Signal()
abd.send(sender=Order, abd1='hey')


@receiver(abd)
def my_task_done(sender, **kwargs):
    print(kwargs)


