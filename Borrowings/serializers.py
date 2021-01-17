from rest_framework import serializers
from Borrowings.models import Borrowing
from Friendlist.serializers import FriendSerializer


class BorrowingSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(read_only=True)
    # Friend = FriendSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = ('Particulars', 'Amount', 'Description', 'Status', 'Friend', 'User')
