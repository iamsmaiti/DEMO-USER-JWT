from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.signals import user_logged_in
from rest_framework_jwt.serializers import jwt_payload_handler
from demo import settings
from rest_framework import status
import jwt
# Create your views here.

class CreateUserAPIView(APIView):
	permission_classes = (AllowAny,)

	def post(self, request):
		user = request.data
		serializer = UserSerializer(data=user)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny,])
def authenticate_user(request):

	try:
		email= request.data['email']
		password = request.data['password']
		user = User.objects.get(email=email, password=password)
		if user:
			try:
				payload = jwt_payload_handler(user)
				token = jwt.encode(payload, settings.SECRET_KEY)
				user_details = {}
				user_details['name'] = "%s %s" % (
					user.first_name, user.last_name)
				user_details['token'] = token
				user_logged_in.send(sender=user.__class__,
					request=request, user=user)
				return Response(user_details, status=status.HTTP_200_ok)
			except Exception as e:
				raise e
		else:
			res = {'error':'can not authenticate with this info. or ac is deactivated'}
			return Response(res, status=status.HTTP_403_FORBIDDEN)
	except keyError:
		res = {'error':'please provide a email and password'}
		return Response(res)

#user_logged_in.send(sender=user.__class__, request=request, user=user) for last login time
'''
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = UserSerializer

	def get(self, request, *args, **kwargs):
		serializer = self.serializer_class(request.user)

		return Response(serializer.data, status=HTTP_200_ok)
	def put(self, request, *args, **kwargs):
		serializer_data = request.data.get('user', {})

		serializer = UserSerializer(
			request.user, data=serializer_data, partial=True
		)
		serializer.is_valid(raise_exception=True)
		return Response(serializer.data, status=status.HTTP_200_ok)
'''

		




