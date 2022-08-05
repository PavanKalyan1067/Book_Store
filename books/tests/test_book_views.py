from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from books.models import Book


class BooksAppTestCases(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='is_staff', email='a6b6@gmail.com', password='123Aabc')
        self.user1 = User.objects.create_user(username='is_not_staff', email='a7b7@gmail.com', password='123Aabc')
        self.book = Book.objects.create(book_title="a1b1",
                                        author="a1b",
                                        price="220",
                                        book_quantity="5",
                                        description="This is a story book",
                                        )

    def test_add_book_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a6b6@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # creating Book pass
        url = reverse('Add_Book')
        book = {
            "book_title": "abd",
            "author": "ab",
            "price": "220",
            "book_quantity": "2",
            "description": "This is a story book",
        }
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.post(url, book, **header)
        # self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_book_api_fail(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # creating Book fail
        url = reverse('Add_Book')
        book = {
            "book_title": "abd",
            "author": "ab",
            "price": "220",
            "book_quantity": "2",
            "description": "This is a story book",
        }
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.post(url, book, **header)
        self.assertEqual(response.data.get('message'), 'Only staff can perform this action')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_book_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a6b6@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # Get All Books pass
        url = reverse('Get_Book')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(url, **header)
        self.assertEqual(response.data.get('message'), 'Success')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_book_api_fail(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # Get All Books fail
        url = reverse('Get_Book')
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.get(url, **header)
        self.assertEqual(response.data.get('message'), 'Something went wrong. Please Try again')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_book_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a6b6@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']

        # del Books pass
        url = reverse('Del_Book', kwargs={'pk': self.book.id})
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.delete(url, **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_fail(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']
        # del Books fail
        url = reverse('Del_Book', kwargs={'pk': self.book.id})
        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.delete(url, **header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_book_by_id_api_pass(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a6b6@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']
        url = reverse('Update_Book', kwargs={"pk": self.book.id})
        # book = self.book()

        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.patch(url, **header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_book_by_id_api_fail(self):
        url = reverse('login')
        # Login successful
        data = {'email': 'a7b7@gmail.com', 'password': '123Aabc'}
        response = self.client.post(url, data)
        token = response.data['data']['tokens']['access']
        url = reverse('Update_Book', kwargs={"pk": self.book.id})
        # book = self.book()

        header = {'Content-Type': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer ' + token}
        response = self.client.patch(url, **header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
