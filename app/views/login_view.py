

from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from app.serializers.login_serializer import LoginSerializer


class LoginAPIView(APIView):

    @swagger_auto_schema(
        request_body=LoginSerializer    ,
        responses={
            status.HTTP_200_OK: "Login successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid Credentials",
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            password = serializer.validated_data.get("password")
            user = authenticate(username=phone_number, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                return Response(data={"Message": "Successfully login",
                                      'access_token': access_token,
                                      'refresh_token': refresh_token},
                                status=status.HTTP_200_OK)
            return Response(data={"Message":"Telefon raqam yoki parol xato"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)