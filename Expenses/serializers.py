from rest_framework import serializers
from Expenses import models


class ExpenseSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Expenses
        fields = '__all__'
