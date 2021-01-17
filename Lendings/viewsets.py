from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Lendings.serializers import LendingSerializer
from Lendings.models import Lending
from Users.models import Account


class LendingsViewSet(ModelViewSet):
    serializer_class = LendingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Lending.objects.filter(User=self.request.user)

    def create(self, request):
        user = Account.objects.get(id=request.user.id)
        serializer = LendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
