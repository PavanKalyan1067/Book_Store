from django.urls import path
from books import views

urlpatterns = [
    path('api/create/', views.AddBookAPI.as_view(), name='Add_Book'),
    path('api/retrieve/', views.GetBookAPI.as_view(), name='Get_Book'),
    path('api/update/<int:pk>/', views.UpdateBookAPI.as_view(), name='Update_Book'),
    path('api/delete/<int:pk>/', views.DeleteBookAPI.as_view(), name='Del_Book'),

]