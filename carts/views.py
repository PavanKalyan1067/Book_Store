from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from accounts.status import response_code
from accounts.views import logger
from carts.models import Cart
from carts.serializers import AddCartSerializer, GetAllCartSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class AddToCartAPI(generics.GenericAPIView):
    serializer_class = AddCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ], request_body=AddCartSerializer)
    def post(self, request):
        data = request.data
        try:
            cart = AddCartSerializer(data=data)
            cart.is_valid(raise_exception=True)
            cart.save()
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


class RetrieveCartAPI(generics.GenericAPIView):
    serializer_class = GetAllCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ])
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        user = request.user
        try:
            cart = Cart.objects.filter(user_id=user)
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


class DeleteCartAPI(generics.GenericAPIView):
    serializer_class = AddCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
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


class UpdateCartAPI(generics.GenericAPIView):
    serializer_class = AddCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            data = request.data
            cart = Cart.objects.get(pk=pk)
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
