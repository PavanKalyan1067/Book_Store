from django.urls import path

from books.views import GetBookAPI, AddBookAPI, DeleteBookAPI, UpdateBookAPI, GetBookAPI1

urlpatterns = [
    path('api/create/', AddBookAPI.as_view(), name='Add_Book'),
    path('api/retrieve/', GetBookAPI.as_view(), name='Get_Book'),
    path('api/retrieve1/', GetBookAPI1.as_view(), name='Get_Book'),
    path('api/update/<int:pk>/', UpdateBookAPI.as_view(), name='Update_Book'),
    path('api/delete/<int:pk>/', DeleteBookAPI.as_view(), name='Del_Book'),

]
