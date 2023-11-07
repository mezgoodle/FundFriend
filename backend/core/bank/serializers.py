from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from core.bank.models import Bank
from core.user.models import User


class BankSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't edit this bank")
        return value

    class Meta:
        model = Bank
        fields = ["id", "author", "description", "edited", "created", "updated"]
        read_only_fields = ["edited"]
