from rest_framework.viewsets import ModelViewSet
from Friendlist.models import Friend
from Friendlist.serializers import FriendSerializer


class FriendlistViewSet(ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
