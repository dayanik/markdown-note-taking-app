import os

from django.db import models


class Note(models.Model):
    note_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="md_files/")

    def save(self, *args, **kwargs):
        if not self.title and self.file:
            self.title = os.path.splitext(os.path.basename(self.file.name))[0]
        return super().save(*args, **kwargs)
