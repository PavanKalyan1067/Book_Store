from django.urls import path

from books.views import BookAPIView

urlpatterns = [
    path('api/create/', BookAPIView.as_view(), name='Add_Book'),
    path('api/retrieve/', BookAPIView.as_view(), name='Get_Book'),
    path('api/update/<int:pk>/', BookAPIView.as_view(), name='Update_Book'),
    path('api/delete/<int:pk>/', BookAPIView.as_view(), name='Del_Book'),
]
