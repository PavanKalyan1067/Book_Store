from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from books.models import Book
from orders.models import Order


class BooksAppTestCases(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='is_not_staff', email='a7b7@gmail.com', password='123Aabc')
        self.book = Book.objects.create(
            book_title="a1b1",
            author="a1b",
            price="220",
            book_quantity="5",
            description="This is a story book",
        )
        self.cart = Order.objects.create(
            book=self.book,
            book_quantity="5",
            total_price=self.book.price,
            user=self.user1
        )

    def test_add_wishlist_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # creating Cart pass
        url = reverse('WishList_Operations')
        cart = {
            "book": self.book.id,
            "book_quantity": "5",
            "user": self.user1.id
        }
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.post(url, cart, **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_wishlist_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # Get All Books pass
        url = reverse('WishList_Operations')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(url, **header)
        self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_wishlist_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # del Books pass
        url = reverse('WishList_Operations', kwargs={'pk': self.cart.id})
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.delete(url, **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



