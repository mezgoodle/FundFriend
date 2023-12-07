from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.bank.models import Bank
from core.bank.serializers import BankSerializer
from core.document.models import Document
from core.user.models import User
from core.user.serializers import UserSerializer


class DocumentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )
    bank = serializers.SlugRelatedField(
        queryset=Bank.objects.all(), slug_field="public_id"
    )

    # def create(self, validated_data):
    #     if not self.context["request"].user.banker:
    #         raise ValidationError("You must be banker to create document")
    #     return super().create(validated_data)

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data["edited"] = True
        return super().update(instance, validated_data)

    def validate_bank(self, value):
        if self.instance:
            return self.instance.bank
        return value

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't edit this document")
        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        bank = Bank.objects.get_object_by_public_id(rep["bank"])
        rep["bank"] = BankSerializer(bank).data
        rep["author"] = UserSerializer(author).data
        return rep

    class Meta:
        model = Document
        fields = [
            "id",
            "author",
            "title",
            "text",
            "bank",
            "edited",
            "created",
            "updated",
        ]
        read_only_fields = ["edited"]
