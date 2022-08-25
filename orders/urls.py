from django.urls import path

from orders.views import OrderAPIView

urlpatterns = [
    path('api/order/', OrderAPIView.as_view(), name='Order_Operations'),
]
