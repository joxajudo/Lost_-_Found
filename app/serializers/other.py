from rest_framework import serializers

from app.models import Category, Item, User, SubCategory, About, AboutCategory, NewsLetter, UserProfile

from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'image']

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
    class Meta:
        model = NewsLetter
        fields = ['id','comment','created_at']


from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'image', 'gender']  # Include any other fields you want to expose through the API.

# I made many changes in this site
