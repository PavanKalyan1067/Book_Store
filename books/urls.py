from django.urls import path

from books.views import BookAPIView

urlpatterns = [
    path('api/book/', BookAPIView.as_view(), name='Book_Operations'),
    path('api/book/<int:pk>/', BookAPIView.as_view(), name='Book_Operations'),
]
