from django.urls import path, include

from app.views.change_password import ChangePasswordView
from app.views.forgot_password import ForgotPasswordView, VerifyForgotPhoneNumberView
from app.views.login_view import LoginAPIView
from app.views.logout_view import LogoutAPIView
from app.views.message import MessageListCreateAPIView, MessageRetrieveAPIView
from app.views.other import (ItemListCreateAPIView, ItemViewSet, CategoryViewSet, SubCategoryViewSet,
                             ItembyCategoryAPIView, ItembyTypeAPIView, ItembyUserAPIView, CurrentUserView,
                             ItembyRequestUserView, AboutCategoryViewSet, AboutViewSet, UserViewSet, NewsLetterViewSet,
                             UserUpdateView, UserProfileListCreateView
                             )
from app.views.register_view import RegisterView
from app.views.verification_code import VerifyPhoneNumberView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # User Profile

    # Register
    path("register/", RegisterView.as_view(), name='register'),
    path("register-verify/", VerifyPhoneNumberView.as_view(), name='register-verify'),

    # Login and Logout
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path("login/", LoginAPIView.as_view(), name='login'),

    # Password
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
    path("forgot-password/", ForgotPasswordView.as_view(), name='forgot-password'),
    path("veriy-forgot-password/", VerifyForgotPhoneNumberView.as_view(), name='verify-forgot-password'),

    # Message
    path('api/messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('api/message/<int:pk>/', MessageRetrieveAPIView.as_view(), name='message-retrieve'),

    # Item
    path('item/', ItemListCreateAPIView.as_view(), name='item'),
    path('item<int:pk>/', ItemViewSet.as_view(), name='item'),
    path('category/', CategoryViewSet.as_view(), name='category'),
    path('sub_category/', SubCategoryViewSet.as_view(), name='sub_category'),

    # Item by user
    path('item/category/<int:category_id>/', ItembyCategoryAPIView.as_view(), name='itembyCategory'),
    path('item/category/<str:type>/', ItembyTypeAPIView.as_view(), name='itembyType'),
    path('item/user/<int:user_id>/', ItembyUserAPIView.as_view(), name='itembyUser'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),

    path('itemss/', ItembyRequestUserView.as_view(), name='itembyUserRequest'),

    # Category
    path('about-category/', AboutCategoryViewSet.as_view(), name='about-category'),
    path('about/', AboutViewSet.as_view(), name='about'),
    path('news-letter/', NewsLetterViewSet.as_view(), name='news-letter'),

    # User-Profile
    path('profile/',UserProfileListCreateView.as_view(),name="profile"),
    path('profile/edit/', UserUpdateView.as_view(), name='profile-edit'),

    path('', include(router.urls))
]
