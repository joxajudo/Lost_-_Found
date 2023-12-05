# serializers.py

from rest_framework import serializers

from app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', 'related_item']


class MessageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
