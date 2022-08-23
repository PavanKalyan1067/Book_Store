from unittest import TestCase

from django.urls import reverse, resolve

from orders.views import OrderAPIView


class TestLabelUrls(TestCase):

    def test_cart_create_url(self):
        url = reverse('Order_Operations')
        self.assertEqual(resolve(url).func.view_class, OrderAPIView)

