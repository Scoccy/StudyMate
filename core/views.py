from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import StudyFile
from .forms import StudyFileForm



def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    files = StudyFile.objects.filter(user=request.user).order_by("-uploaded_at")

    if request.method == "POST":
        form = StudyFileForm(request.POST, request.FILES)

        if form.is_valid():
            study_file = form.save(commit=False)
            study_file.user = request.user

            if not study_file.title:
                study_file.title = study_file.pdf.name

            study_file.save()
            return redirect("dashboard")
    else:
        form = StudyFileForm()

    return render(request, "dashboard.html", {
        "files": files,
        "form": form
    })


@login_required
def create_summary(request):
    if request.method == 'POST':
        form = SummaryForm(request.POST)

        if form.is_valid():
            summary = form.save(commit=False)
            summary.user = request.user
            summary.save()
            return redirect('dashboard')
    else:
        form = SummaryForm()

    return render(request, 'core/form_page.html', {
        'form': form,
        'title': 'Create Summary',
    })


@login_required
def create_mindmap(request):
    if request.method == 'POST':
        form = MindMapForm(request.POST)

        if form.is_valid():
            mindmap = form.save(commit=False)
            mindmap.user = request.user
            mindmap.save()
            return redirect('dashboard')
    else:
        form = MindMapForm()

    return render(request, 'core/form_page.html', {
        'form': form,
        'title': 'Create Mind Map',
    })


@login_required
def create_studyplan(request):
    if request.method == 'POST':
        form = StudyPlanForm(request.POST)

        if form.is_valid():
            studyplan = form.save(commit=False)
            studyplan.user = request.user
            studyplan.save()
            return redirect('dashboard')
    else:
        form = StudyPlanForm()

    return render(request, 'core/form_page.html', {
        'form': form,
        'title': 'Create Study Plan',
    })


@login_required
def create_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)

        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('dashboard')
    else:
        form = ReminderForm()

    return render(request, 'core/form_page.html', {
        'form': form,
        'title': 'Create Reminder',
    })

@login_required
def dashboard(request):
    files = StudyFile.objects.filter(user=request.user).order_by("-uploaded_at")

    if request.method == "POST":
        form = StudyFileForm(request.POST, request.FILES)

        if form.is_valid():
            study_file = form.save(commit=False)
            study_file.user = request.user

            if not study_file.title:
                study_file.title = study_file.pdf.name

            study_file.save()
            return redirect("dashboard")
    else:
        form = StudyFileForm()

    return render(request, "dashboard.html", {
        "files": files,
        "form": form
    })

@login_required
def delete_file(request, file_id):
    study_file = get_object_or_404(StudyFile, id=file_id, user=request.user)

    if request.method == "POST":
        if study_file.pdf:
            study_file.pdf.delete(save=False)

        study_file.delete()
        return redirect("dashboard")

    return redirect("dashboard")


@login_required
def generate_summary(request, file_id):
    study_file = get_object_or_404(StudyFile, id=file_id, user=request.user)

    if request.method == "POST":
        import os

        ai_enabled = os.environ.get("ENABLE_AI_SUMMARY", "True") == "True"

        if not ai_enabled:
            study_file.summary = "AI summary is disabled on the online demo because the free server does not have enough memory for the AI model."
            study_file.summary_created_at = timezone.now()
            study_file.save()
            return redirect("summaries")

        from .ai_summary import generate_pdf_summary

        pdf_path = study_file.pdf.path
        summary = generate_pdf_summary(pdf_path)

        study_file.summary = summary
        study_file.summary_created_at = timezone.now()
        study_file.save()

    return redirect("summaries")