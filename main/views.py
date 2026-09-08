from django.shortcuts import render

from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Ahmad Hoesin",
        "npm": "2506555400",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and DevOps."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ahmad Hoesin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_projects(request):
    context = {
        "name": "Ahmad Hoesin",
        "projects_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)