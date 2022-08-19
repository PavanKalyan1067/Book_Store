from rest_framework import status, permissions, generics
from rest_framework.response import Response

from accounts import logger
from accounts.status import response_code, CustomExceptions
from .models import Wishlist
from .serializers import WishlistSerializer, GetWishlistSerializer


class AddToWishlistAPI(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistSerializer

    def post(self, request):
        try:
            wishlist_serializer = WishlistSerializer(data=request.data)
            wishlist_serializer.is_valid(raise_exception=True)
            # book = Wishlist.objects.get(book=wishlist_serializer.data.get('book'))
            # if book:
            #     raise CustomExceptions.BookAlreadyExists('book already exists in your wishlist', 400)
            wishlist_serializer.save()
            response = {
                'message': 'book added to wishlist',
                'status_code': 200,
                'data': wishlist_serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)


class GetWishlistAPIView(generics.GenericAPIView):

    def get(self, request):
        try:
            user = request.user
            if user:
                wishlist = Wishlist.objects.filter(user_id=user)
                if not wishlist:
                    raise CustomExceptions.CartDoesNotExist('Add to wishlist at first', 400)
                if wishlist:
                    wishlist_serializer = GetWishlistSerializer(wishlist, many=True)
                    response = {
                        'success': True,
                        'message': response_code[200],
                        'data': wishlist_serializer.data
                    }
                    return Response(response, status=status.HTTP_200_OK)
                return Response(status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
