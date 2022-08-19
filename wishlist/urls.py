from django.urls import path

from wishlist.views import AddToWishlistAPI, GetWishlistAPIView, DeleteWishlistAPI

urlpatterns = [
    path('api/add/', AddToWishlistAPI.as_view(), name="add_to_wishlist"),
    path('api/retrieve/', GetWishlistAPIView.as_view(), name="get_wishlist"),
    path('api/delete/<int:pk>/', DeleteWishlistAPI.as_view(), name='delete_cart'),

]
