from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="public_id", read_only=True, format="hex")
    created = serializers.DateTimeField(read_only=True, source="created_at")
    updated = serializers.DateTimeField(read_only=True, source="updated_at")
