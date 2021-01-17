from rest_framework import serializers
from Expenses.models import Expenses


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('Particulars', 'Amount', 'Date', 'Status')
