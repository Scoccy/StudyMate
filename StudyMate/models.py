from django.db import models
from django.contrib.auth.models import User


class StudyFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_files")
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title