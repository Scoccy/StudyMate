from django import forms
from .models import StudyFile, Summary, MindMap, StudyPlan, Reminder


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Summary text',
        }


class MindMapForm(forms.ModelForm):
    class Meta:
        model = MindMap
        fields = ['title', 'content']
        labels = {
            'title': 'Title',
            'content': 'Mind map content',
        }


class StudyPlanForm(forms.ModelForm):
    class Meta:
        model = StudyPlan
        fields = ['subject', 'goal', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'date', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


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