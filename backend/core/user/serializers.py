from rest_framework import serializers

from core.user.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source="public_id", read_only=True, format="hex"
    )
    created = serializers.DateTimeField(read_only=True, source="created_at")
    updated = serializers.DateTimeField(read_only=True, source="updated_at")

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
        ]
        read_only_fields = ["is_active"]
