from django.urls import path

from carts.views import CartAPI

urlpatterns = [
    path('api/create/', CartAPI.as_view(), name='add_to_cart'),
    path('api/retrieve/', CartAPI.as_view(), name='get_cart'),
    path('api/update/<int:pk>/', CartAPI.as_view(), name='update_cart'),
    path('api/delete/<int:pk>/', CartAPI.as_view(), name='delete_cart'),
]
