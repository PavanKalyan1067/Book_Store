from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from books.models import Book
from carts.models import Cart


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
        self.cart = Cart.objects.create(
            book=self.book,
            book_quantity="5",
            total_price=self.book.price,
            user=self.user1
        )

    def test_add_cart_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # creating Cart pass
        url = reverse('add_to_cart')
        cart = {
            "book": self.book.id,
            "book_quantity": "5",
            "user": self.user1.id
        }
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.post(url, cart, **header)
        self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_cart_api_fail(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # creating Cart Fail
        url = reverse('add_to_cart')
        book = {
            "book": "3",
            "book_quantity": "5",
            "user": self.user1.id
        }
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.post(url, book, **header)
        self.assertEqual(response.data.get('message'), 'Something went wrong. Please Try again')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_cart_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # Get All Books pass
        url = reverse('get_cart')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(url, **header)
        self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_cart_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # del Books pass
        url = reverse('delete_cart', kwargs={'pk': self.cart.id})
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.delete(url, **header)
        self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_cart_by_id_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']
        url = reverse('update_cart', kwargs={"pk": self.cart.id})

        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.patch(url, **header)
        self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

