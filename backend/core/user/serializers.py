from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "bio",
            "avatar",
            "created",
            "updated",
            "is_active",
            "full_name",
        ]
        read_only_fields = ["is_active"]
