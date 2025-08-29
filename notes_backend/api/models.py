from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base model providing created and updated timestamp fields."""
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the record was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the record was last updated")

    class Meta:
        abstract = True


# PUBLIC_INTERFACE
class Note(TimeStampedModel):
    """
    Represents a note entity.

    Fields:
    - title: Short title for the note (required).
    - content: Body of the note (optional, can be blank).
    - created_at: Auto timestamp when created.
    - updated_at: Auto timestamp when updated.
    """
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField(blank=True, default="")

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self) -> str:
        return f"{self.title}"
