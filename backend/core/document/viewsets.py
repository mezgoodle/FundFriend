from django.http.response import Http404
from rest_framework import status
from rest_framework.response import Response

from core.abstract.viewsets import AbstractViewSet
from core.auth.permissions import UserPermission
from core.document.models import Document
from core.document.serializers import DocumentSerializer


class DocumentViewSet(AbstractViewSet):
    http_method_names = ("get", "post", "put", "delete", "patch")
    permission_classes = (UserPermission,)
    serializer_class = DocumentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Document.objects.all()
        if not (bank_pk := self.kwargs.get("bank_pk")):
            return Http404
        return Document.objects.filter(bank__public_id=bank_pk)

    def get_object(self):
        obj = Document.objects.get_object_by_public_id(self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
