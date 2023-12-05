from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from app.models import Message, Item
from app.permission import IsSenderOrReciever
from app.serializers.message import MessageSerializer, MessageGetSerializer


class MessageListCreateAPIView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsSenderOrReciever]  # Apply the custom permission

    def get_queryset(self):
        # Filter messages based on the related item and involved users
        item_id = self.request.query_params.get('related_item')

        queryset = Message.objects.filter(
            Q(sender=self.request.user) |
            Q(receiver=self.request.user)
        )

        return queryset

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user,
                        receiver=Item.objects.filter(id=self.request.data['related_item']).first().user)


class MessageRetrieveAPIView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageGetSerializer
    permission_classes = [IsSenderOrReciever]
