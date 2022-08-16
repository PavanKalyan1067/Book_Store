from django.urls import path

from orders.views import OrderAPIView, GetOrderAPIView

urlpatterns = [
    path('api/checkout/', OrderAPIView.as_view(), name='checkout'),
    path('api/get-orders/', GetOrderAPIView.as_view(), name='get-orders'),
]
