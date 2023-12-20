from django.urls import path, include

from app.views.change_password import ChangePasswordView
from app.views.forgot_password import ForgotPasswordView, VerifyForgotPhoneNumberView
from app.views.login_view import LoginAPIView
from app.views.logout_view import LogoutAPIView
from app.views.message import MessageListCreateAPIView, MessageRetrieveAPIView
from app.views.other import ItemViewSet, ItemListCreateAPIView, CategoryViewSet, UserViewSet, SubCategoryViewSet
from app.views.register_view import RegisterView
from app.views.verification_code import VerifyPhoneNumberView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("register-verify/", VerifyPhoneNumberView.as_view(), name='register-verify'),
    path("login/", LoginAPIView.as_view(), name='login'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
    path("forgot-password/", ForgotPasswordView.as_view(), name='forgot-password'),
    path("veriy-forgot-password/", VerifyForgotPhoneNumberView.as_view(), name='verify-forgot-password'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('api/message/<int:pk>/', MessageRetrieveAPIView.as_view(), name='message-retrieve'),

    path('item/', ItemListCreateAPIView.as_view(), name='item'),
    path('item<int:pk>/', ItemViewSet.as_view(), name='item'),
    path('category/', CategoryViewSet.as_view(), name='category'),
    path('sub_category/', SubCategoryViewSet.as_view(), name='sub_category'),
    path('', include(router.urls))
]
