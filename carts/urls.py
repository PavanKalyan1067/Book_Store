from django.urls import path

from carts.views import AddToCartAPI, RetrieveCartAPI, UpdateCartAPI, DeleteCartAPI

urlpatterns = [
    path('api/create/', AddToCartAPI.as_view(), name='add_to_cart'),
    path('api/retrieve/', RetrieveCartAPI.as_view(), name='get_cart'),
    path('api/update/<int:pk>/', UpdateCartAPI.as_view(), name='update_cart'),
    path('api/delete/<int:pk>/', DeleteCartAPI.as_view(), name='delete_cart'),

]
