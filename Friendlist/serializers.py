from rest_framework import serializers
from Friendlist.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    #User = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Friend
        fields = '__all__'
