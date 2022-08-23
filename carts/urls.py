from django.urls import path

from carts.views import CartAPI

urlpatterns = [
    path('api/cart/', CartAPI.as_view(), name='Cart_Operations'),
    path('api/cart/<int:pk>/', CartAPI.as_view(), name='Cart_Operations'),
]
