from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from accounts.status import response_code
from accounts.views import logger
from carts.serializers import AddCartSerializer, GetAllCartSerializer
from orders.models import Order


class CartAPI(generics.GenericAPIView):
    """
    CartAPI is for perform CURD operation for order
    """
    serializer_class = AddCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ], request_body=AddCartSerializer)
    def post(self, request):
        """
        post method is for add to cart to place the order
        """
        try:
            cart = AddCartSerializer(data=request.data)
            cart.is_valid(raise_exception=True)
            cart.save(user_id=request.user.id)
            response = {
                'success': True,
                'message': response_code[200],
                'data': cart.data
            }
            return Response(response)

        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ])
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        """
        GET Method is for get the cart for users
        """
        user = request.user
        try:
            cart = Order.objects.filter(user_id=user)
            serializer = GetAllCartSerializer(cart, many=True)
            response = {
                'success': True,
                'message': response_code[200],
                'data': serializer.data
            }
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete method is for delete the cart by id
        """
        try:
            cart = Order.objects.get(pk=pk, user_id=request.user.id)
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

    def patch(self, request, pk):
        """
        Update method is for update the cart by id
        """
        try:
            data = request.data
            cart = Order.objects.get(pk=pk, user_id=request.user.id)
            serializer = AddCartSerializer(cart, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {
                'success': True,
                'message': response_code[200],
                'data': serializer.data
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
