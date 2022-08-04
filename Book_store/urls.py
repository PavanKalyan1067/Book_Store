from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Book Store')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Book_Store/', schema_view),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('carts/', include('carts.urls')),

]
