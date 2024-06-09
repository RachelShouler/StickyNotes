# Import necessary modules
from django.db import models
# from django.contrib.auth.models import User


# Create a model for Sticky Notes
class StickyNotes(models.Model):
    # Title of the sticky note
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()    # Content of the sticky note
    # Timestamp when the sticky note was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # Return the title as the string representation of the model
