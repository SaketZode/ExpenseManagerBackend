from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from Expenses import models
from Expenses import serializers
from Users.models import Account


class ExpensesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return models.Expenses.objects.filter(User=self.request.user)

    def create(self, request):
        EndUser = Account.objects.get(id=request.user.id)
        serializer = serializers.ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=EndUser)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
