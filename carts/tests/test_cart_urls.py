from unittest import TestCase

from django.urls import reverse, resolve

from carts.views import CartAPI


class TestLabelUrls(TestCase):

    def test_cart_create_url(self):
        url = reverse('add_to_cart')
        self.assertEqual(resolve(url).func.view_class, CartAPI)

    def test_cart_get_url(self):
        url = reverse('get_cart')
        self.assertEqual(resolve(url).func.view_class, CartAPI)

    def test_cart_update_url(self):
        url = reverse('update_cart', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, CartAPI)
