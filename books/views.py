from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.settings import api_settings

from accounts import logger
from accounts.models import User
from accounts.status import response_code, DoesNotExist
from books.models import Book
from books.serializers import AddBookSerializer, BookSerializer
from books.utils import BookRedis


def get_user(token):
    jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
    newToken = str(token).split("Bearer ")[1]
    encodedToken = jwt_decode_handler(newToken)
    username = encodedToken['username']
    user = User.objects.get(username=username)
    return user.id


class AddBookAPI(generics.GenericAPIView):
    serializer_class = AddBookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            user = request.user.is_staff
            if request.user.is_staff:
                data = request.data
                book = AddBookSerializer(data=data)
                book.is_valid(raise_exception=True)
                book.save()
                BookRedis.update(user=user, book_dict=book.data)
                response = {
                    'success': True,
                    'message': response_code[200],
                    'data': book.data
                }
                return Response(response)
            response = {
                'success': False,
                'message': "Only staff can perform this action",
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)}
            logger.exception(str(e))
            return Response(response)


class GetBookAPI(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            if user.is_staff:
                all_books = Book.objects.all()
                book_s = BookSerializer(all_books, many=True)
                response = {
                    'success': True,
                    'message': response_code[200],
                    'data': book_s.data
                }
                return Response(response)
            response = {
                'success': False,
                'message': response_code[416],
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        except DoesNotExist as e:
            response = {
                'success': False,
                'message': response_code[307],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)


class GetBookAPI1(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = request.user.is_staff
            if user.is_staff:
                book_s = BookRedis.extract(user=user)
                response = {
                    'success': True,
                    'message': response_code[200],
                    'data': book_s.data
                }
                return Response(response)
            response = {
                'success': False,
                'message': response_code[416],
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        except DoesNotExist as e:
            response = {
                'success': False,
                'message': response_code[307],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)


class UpdateBookAPI(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        user = request.user
        try:
            if user.is_staff:
                book = Book.objects.get(pk=pk)
                book = BookSerializer(book, request.data, partial=True)
                book.is_valid(raise_exception=True)
                book.save()
                response = {
                    'success': True,
                    'message': response_code[200],
                    'data': book.data
                }
                return Response(response)
            return Response({'success': False, 'message': 'Book not updated'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)}
            logger.exception(str(e))
            return Response(response)


class DeleteBookAPI(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        user = request.user
        try:
            if user.is_staff:
                book = Book.objects.get(pk=pk)
                book.delete()
                response = {
                    'success': True,
                    'message': response_code[200],
                }
                return Response(response)
            return Response({'success': False, 'message': 'user not a staff'}, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist as e:
            response = {
                'success': False,
                'message': response_code[307],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
