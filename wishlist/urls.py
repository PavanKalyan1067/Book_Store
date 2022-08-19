from django.urls import path
from wishlist.views import AddToWishlistAPI, GetWishlistAPIView

urlpatterns = [
    path('api/add/', AddToWishlistAPI.as_view(), name="adding_to_wishlist"),
    path('api/retrieve/', GetWishlistAPIView.as_view(), name="view_wishlist"),
]