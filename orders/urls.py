from django.urls import path

from orders.views import OrderAPIView

urlpatterns = [
    path('api/checkout/', OrderAPIView.as_view(), name='checkout'),
    path('api/get-orders/', OrderAPIView.as_view(), name='get-orders'),
]
