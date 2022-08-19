from unittest import TestCase

from django.urls import reverse, resolve

from wishlist.views import DeleteWishlistAPI, GetWishlistAPIView, AddToWishlistAPI


class TestLabelUrls(TestCase):

    def test_cart_create_url(self):
        url = reverse('add_to_wishlist')
        self.assertEqual(resolve(url).func.view_class, AddToWishlistAPI)

    def test_cart_get_url(self):
        url = reverse('get_wishlist')
        self.assertEqual(resolve(url).func.view_class, GetWishlistAPIView)

    def test_cart_delete_url(self):
        url = reverse('delete_cart', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, DeleteWishlistAPI)
