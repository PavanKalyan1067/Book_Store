from unittest import TestCase

from django.urls import reverse, resolve

from carts.views import CartAPI


class TestLabelUrls(TestCase):

    def test_cart_create_url(self):
        url = reverse('Cart_Operations')
        self.assertEqual(resolve(url).func.view_class, CartAPI)

    def test_cart_update_url(self):
        url = reverse('Cart_Operations', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, CartAPI)
