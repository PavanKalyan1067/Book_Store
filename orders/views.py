from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework import status, permissions, generics
from rest_framework.response import Response

from accounts.status import response_code, CustomExceptions
from accounts.views import logger

from orders.models import Order
from orders.serializers import OrderSerializer, GetOrderSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class OrderAPIView(generics.GenericAPIView):
    """
    OrderAPIView is for place the order
    """
    serializer_class = OrderSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ], request_body=OrderSerializer)
    def post(self, request):
        try:
            data = request.data
            order = OrderSerializer(data=data)
            order.is_valid(raise_exception=True)
            cart = (order.validated_data.get('cart'))
            order.save()
            response = {
                'success': True,
                'message': response_code[200], f'order has been placed by {cart.user.username}'
                                               'data': order.data
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


class GetOrderAPIView(generics.GenericAPIView):
    """
    GetOrderAPIView is for get the order by user and all the details
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetOrderSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ])
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        try:
            user = request.user
            if user:
                order = Order.objects.filter(user_id=user, cart__ordered=True)
                if not order:
                    raise CustomExceptions.CartDoesNotExist('Create order at first', 400)
                if order:
                    cart_serializer = GetOrderSerializer(order, many=True)
                    response = {
                        'success': True,
                        'message': response_code[200],
                        'data': cart_serializer.data
                    }
                    return Response(response, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response = {
                'success': False,
                'message': response_code[416],
                'data': str(e)
            }
            logger.exception(e)
            return Response(response)
