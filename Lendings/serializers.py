from rest_framework import serializers
from Lendings.models import Lending


class LendingSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Lending
        fields = ('Particulars', 'Amount', 'Description', 'Status', 'Friend', 'User')
