from unittest import TestCase

from django.urls import reverse, resolve

from wishlist.views import WishlistAPIView


class TestLabelUrls(TestCase):

    def test_cart_create_url(self):
        url = reverse('WishList_Operations')
        self.assertEqual(resolve(url).func.view_class, WishlistAPIView)

    def test_cart_delete_url(self):
        url = reverse('WishList_Operations', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, WishlistAPIView)
