from django.urls import path

from orders.views import OrderAPI, GetOrderAPI

urlpatterns = [
    path('api/checkout/', OrderAPI.as_view(), name='checkout'),
    path('api/get-orders/', GetOrderAPI.as_view(), name='get-orders'),
]
