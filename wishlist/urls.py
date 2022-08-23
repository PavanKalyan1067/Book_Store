from django.urls import path

from wishlist.views import WishlistAPIView

urlpatterns = [
    path('api/wishlist/', WishlistAPIView.as_view(), name='WishList_Operations'),
    path('api/wishlist/<int:pk>/', WishlistAPIView.as_view(), name='WishList_Operations'),

]
