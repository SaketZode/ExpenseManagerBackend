from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet
from Borrowings.models import Borrowing
from Borrowings.serializers import BorrowingSerializer
from Users.models import Account


class BorrowingsViewSet(ModelViewSet):
    serializer_class = BorrowingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Borrowing.objects.filter(User=self.request.user)

    def create(self, request):
        user = Account.objects.get(id=request.user.id)
        serializer = BorrowingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
