from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class StudyFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_files")
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    summary = models.TextField(blank=True, null=True)
    summary_created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Summaries"

    def __str__(self):
        return self.title


class MindMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    goal = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    date = models.DateField()
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title