from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response

from accounts.status import response_code
from accounts.views import logger
from orders.models import Order
from orders.serializers import OrderSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class OrderAPIView(generics.GenericAPIView):
    """
    OrderAPIView is for place the order
    """
    serializer_class = OrderSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, "token", type=openapi.TYPE_STRING)
    ], request_body=OrderSerializer)
    def post(self, request):
        """
        POST Method is for place the order
        """
        try:
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user_id=request.user.id)
            response = {
                'success': True,
                'message': response_code[200],
                'data': serializer.data
            }
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
        GET Method is for get the order by user and all the details
        """
        try:
            user = request.user
            if 'order' in cache:
                order1 = cache.get('order')
                response = {
                    'order': order1,
                    'message': 'Getting All The data from cache',
                }
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                orders = Order.objects.filter(user_id=user)
                ord = [order.order() for order in orders]
                cache.set(orders, ord, timeout=CACHE_TTL)
                response = {
                    'success': True,
                    'message': 'Getting All The data',
                    'data': ord,
                }
                return Response(response, status.HTTP_200_OK)

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
        Update method is for update the order by id
        """
        try:
            order = Order.objects.get(pk=pk, user_id=request.user.id)
            serializer = OrderSerializer(order, data=request.data, partial=True)
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

    def delete(self, request, pk):
        """
        Delete method is for delete the order by id
        """
        try:
            user = request.user
            order = Order.objects.get(pk=pk, user_id=user.id)
            order.delete()
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
