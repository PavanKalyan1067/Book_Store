from django.urls import path

from wishlist.views import AddToWishlistAPI, GetWishlistAPIView, DeleteWishlistAPI

urlpatterns = [
    path('api/add/', AddToWishlistAPI.as_view(), name="adding_to_wishlist"),
    path('api/retrieve/', GetWishlistAPIView.as_view(), name="view_wishlist"),
    path('api/delete/<int:pk>/', DeleteWishlistAPI.as_view(), name='delete_cart'),

]
