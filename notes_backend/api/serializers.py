from rest_framework import serializers
from .models import Note


# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializer for Note model handling validation and serialization for API I/O."""

    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_title(self, value: str) -> str:
        """Ensure the title is not empty or whitespace-only."""
        if value is None or str(value).strip() == "":
            raise serializers.ValidationError("Title cannot be empty.")
        return value
