import jwt

from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from rest_framework import generics
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.logger import get_logger
from accounts.status import response_code
from accounts.utils import Util
from accounts.models import User
from accounts.renderers import UserRenderer
from accounts.serializers import (
    RegisterSerializer,
    EmailVerificationSerializer,
    UserPasswordResetSerializer,
    ForgotPasswordSerializer,
    LoginSerializer,
    LogoutSerializer,
)

logger = get_logger()

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER


class Home(TemplateView):
    template_name = 'Home.html'


class RegisterView(generics.GenericAPIView):
    """
    RegisterView(generics.GenericAPIView) is for registering a new user
    """
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        try:
            user = request.data
            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink = reverse('email-verify')
            absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
            email_body = 'Hi ' + user.username + \
                         ' Use the link below to verify your email \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email, 'from_email': settings.EMAIL_HOST_USER,
                    'email_subject': 'Verify your email'}
            Util.send_email(data)
            response = {
                'success': True,
                'msg': response_code[200],
                'data': user_data
            }
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': 'Oops! Something went wrong! Please try again...',
                'data': str(e)
            }
            logger.exception(str(e))
            return Response(response)


class VerifyEmail(generics.GenericAPIView):
    """
    VerifyEmail(generics.GenericAPIView) is for Verifying email for new user after registration
    """
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            print('payload 1 ' + str(payload))
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
                response = {
                    'status': True,
                    'msg': response_code[302]
                }
                return Response(response)
        except jwt.ExpiredSignatureError as e:
            response = {
                'status': True,
                'msg': response_code[304],
                'data': str(e)
            }
            logger.exception(str(e))
            return Response(response)
        except jwt.exceptions.DecodeError as e:
            response = {
                'status': True,
                'msg': response_code[307],
                'data': str(e)
            }
            logger.exception(str(e))
            return Response(response)


class ForgotPasswordResetEmailAPIView(generics.GenericAPIView):
    """
    ForgotPasswordResetEmailAPIView(generics.GenericAPIView) is for it will send the link to email to reset the
    password for existing user
    """
    renderer_classes = [UserRenderer]
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        try:
            serializer = ForgotPasswordSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            response = {
                'status': True,
                'msg': response_code[309]
            }
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': 'Oops! Something went wrong! Please try again...',
                'data': str(e)
            }
            logger.exception(str(e))
            return Response(response)


class SetNewPasswordAPIView(generics.GenericAPIView):
    """
    SetNewPasswordAPIView(generics.GenericAPIView) is for updating new password for Existing user
    """
    renderer_classes = [UserRenderer]
    serializer_class = UserPasswordResetSerializer

    def post(self, request, uid, token):
        try:
            serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
            serializer.is_valid(raise_exception=True)
            response = {
                'status': True,
                'msg': response_code[308]
            }
            return Response(response)
        except Exception as e:
            response = {
                'success': False,
                'message': 'Oops! Something went wrong! Please try again...',
                'data': str(e)
            }
            logger.exception(str(e))
            return Response(response)


class LogoutAPIView(generics.GenericAPIView):
    """
    LogoutAPIView(generics.GenericAPIView) is for logging out the user
    """
    serializer_class = LogoutSerializer

    def get(self, request):
        return render(request, 'logout.html')

    def post(self, request):
        try:
            Refresh_token = request.data["refresh"]
            token = RefreshToken(Refresh_token)
            token.blacklist()
            response = ({
                'success': True,
                'msg': response_code[417]
            })
            return Response(response)
        except Exception as e:
            response = ({
                'success': False,
                'msg': response_code[418],
                'data': str(e)
            })
            logger.exception(str(e))
            return Response(response)


class UserProfileView(generics.GenericAPIView):
    """
    UserProfileView(generics.GenericAPIView) is for get all the users who have registered
    """
    renderer_classes = [UserRenderer]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def get(self, request):
        try:
            user = User.objects.all()
            allUser = RegisterSerializer(user, many=True)
            response = ({
                'Success': True,
                'msg': response_code[200],
                'data': allUser.data
            })
            return Response(response)
        except Exception as e:
            response = ({
                'success': False,
                'msg': response_code[416],
                'data': str(e)
            })
            logger.exception(str(e))
            return Response(response)


class LoginAPIView(generics.GenericAPIView):
    """
    LoginAPIView(generics.GenericAPIView) is for Login for user who have registered
    """
    serializer_class = LoginSerializer

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            response = {
                'status': True,
                'msg': response_code[419],
                'data': serializer.data
            }
            return Response(response)
        except Exception as e:
            response = ({
                'success': False,
                'msg': response_code[416],
                'data': str(e)
            })
            logger.exception(str(e))
            return Response(response)
