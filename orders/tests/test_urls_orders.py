from unittest import TestCase

from django.urls import reverse, resolve

from orders.views import OrderAPI, GetOrderAPI


class TestLabelUrls(TestCase):

    def test_cart_create_url(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func.view_class, OrderAPI)

    def test_cart_get_url(self):
        url = reverse('get-orders')
        self.assertEqual(resolve(url).func.view_class, GetOrderAPI)
