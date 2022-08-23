from django.urls import path

from wishlist.views import WishlistAPIView

urlpatterns = [
    path('api/add/', WishlistAPIView.as_view(), name="add_to_wishlist"),
    path('api/retrieve/', WishlistAPIView.as_view(), name="get_wishlist"),
    path('api/delete/<int:pk>/', WishlistAPIView.as_view(), name='delete_cart'),

]
