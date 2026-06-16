from django import forms
from .models import StudyFile


class StudyFileForm(forms.ModelForm):
    class Meta:
        model = StudyFile
        fields = ["title", "pdf"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "input",
                "placeholder": "File title"
            }),
            "pdf": forms.FileInput(attrs={
                "class": "input",
                "accept": "application/pdf"
            }),
        }