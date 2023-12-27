from rest_framework import serializers

from app.models import Category, Item, User, SubCategory, About, AboutCategory, NewsLetter, UserProfile
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'image','password','phone_number']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.image = validated_data.get('image', instance.image)

        instance.save()
        return instance


class AboutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCategory
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'image', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'image', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'image', 'username', 'phone_number')


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NewsLetterSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username', read_only=True)
    user_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = NewsLetter
        fields = ['id', 'user', 'user_username', 'user_image', 'comment', 'created_at']

    def get_user_image(self, instance):
        user = instance.user
        if user and hasattr(user, 'image') and user.image:
            return user.image.url
        return None
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(NewsLetterSerializer, self).create(validated_data)


from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['image', 'gender']  # Include any other fields you want to expose through the API.

class ExtendedUserProfileSerializer(UserProfileSerializer):
    phone_number = serializers.CharField(allow_blank=True)
    password = serializers.CharField(write_only=True, validators=[MinLengthValidator(limit_value=8)])
    password_confirm = serializers.CharField(write_only=True)

    class Meta(UserProfileSerializer.Meta):
        fields = UserProfileSerializer.Meta.fields + ['phone_number', 'password', 'password_confirm']
# I made many changes in this site
