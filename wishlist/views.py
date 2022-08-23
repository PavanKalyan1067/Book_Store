from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, generics
from rest_framework.response import Response

from accounts import logger
from accounts.status import response_code, CustomExceptions
from orders.models import Order
from wishlist.serializers import WishlistSerializer, GetWishlistSerializer


class WishlistAPIView(generics.GenericAPIView):
    """
    WishlistAPIView is for Add and Get Book for wishlist by user
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ], request_body=WishlistSerializer)
    def post(self, request):
        """
        POST Method is for Add Book for wishlist by user
        """
        try:
            wishlist = WishlistSerializer(data=request.data)
            wishlist.is_valid(raise_exception=True)
            wishlist.save(user_id=request.user.id)
            response = {
                'message': 'book added to wishlist',
                'status_code': 200,
                'data': wishlist.data}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ])
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        """
        GET Method is for Get Book for wishlist by user
        """
        try:
            user = request.user
            if user:
                wishlist = Order.objects.filter(user_id=user)
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

    def delete(self, request, pk):
        """
        Delete method is for delete wishlist book by id
        """
        try:
            cart = Order.objects.get(pk=pk)
            cart.delete()
            response = {
                'success': True,
                'message': response_code[200],
            }
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
