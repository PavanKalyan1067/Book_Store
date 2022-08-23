from unittest import TestCase

from django.urls import reverse, resolve
from books.views import BookAPIView


class TestLabelUrls(TestCase):

    def test_book_create_and_get_url(self):
        url = reverse('Book_Operations')
        self.assertEqual(resolve(url).func.view_class, BookAPIView)

    def test_book_update_and_delete_url(self):
        url = reverse('Book_Operations', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, BookAPIView)
