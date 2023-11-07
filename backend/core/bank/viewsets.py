from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.abstract.viewsets import AbstractViewSet
from core.bank.models import Bank
from core.bank.serializers import BankSerializer


class BankViewSet(AbstractViewSet):
    http_method_names = ("get", "post")
    permission_classes = (IsAuthenticated,)
    serializer_class = BankSerializer

    def get_queryset(self):
        return Bank.objects.all()

    def get_object(self):
        obj = Bank.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
