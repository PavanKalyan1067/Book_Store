from unittest import TestCase

from django.urls import reverse, resolve
from books.views import AddBookAPI, UpdateBookAPI, DeleteBookAPI, GetBookAPI


class TestLabelUrls(TestCase):

    def test_book_create_url(self):
        url = reverse('Add_Book')
        self.assertEqual(resolve(url).func.view_class, AddBookAPI)

    def test_book_get_url(self):
        url = reverse('Get_Book')
        self.assertEqual(resolve(url).func.view_class, GetBookAPI)

    def test_book_update_url(self):
        url = reverse('Update_Book', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, UpdateBookAPI)

    def test_book_delete_url(self):
        url = reverse('Del_Book', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, DeleteBookAPI)
