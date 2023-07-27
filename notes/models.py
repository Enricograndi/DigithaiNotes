from django.contrib.auth.models import User
from django.db import models

class Notes(models.Model):
    # ForeignKey to link each note to a specific user. on_delete=models.CASCADE means if the user is deleted, their associated notes will also be deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Title of the note, stored as a TextField in the database.
    title = models.TextField()

    # Content or text of the note, also stored as a TextField in the database.
    text = models.TextField()

    # DateTimeField that stores the creation date and time of the note. auto_now_add=True means it will be automatically set to the current date and time when a note is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # DateTimeField that stores the last update date and time of the note. auto_now=True means it will be automatically updated to the current date and time whenever a note is modified.
    updated_at = models.DateTimeField(auto_now=True)
