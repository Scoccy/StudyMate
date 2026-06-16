from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudyFile
from .forms import StudyFileForm


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