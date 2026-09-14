from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.models import Experience, Project
from main.forms import ExperienceForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings


def add_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        submitted_code = request.POST.get("secret_code")
        if submitted_code != settings.PORTFOLIO_SECRET_CODE:
            messages.error(request, "Incorrect secret code. You do not have permission to add an experience.")
            context = {
                "name": "Ahmad Hoesin",
                "form": form,
            }
            return render(request, "experience_form.html", context)
        
        form.save()
        messages.success(request, "New Experience Added!")
        return redirect("main:show_experience")

    context = {
        "name": "Ahmad Hoesin",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def show_main(request):
    context = {
        "name": "Ahmad Hoesin",
        "npm": "25065&#8203;55400",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and DevOps."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)
    
    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )
    experience = [experience.object for experience in experience]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Ahmad Hoesin",
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def show_projects(request):
    context = {
        "name": "Ahmad Hoesin",
        "projects_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def delete_experience(request, experience_id):
        experience = get_object_or_404(Experience, pk=experience_id)
        if request.method == "POST":
            submitted_code = request.POST.get("secret_code")
            if submitted_code != settings.PORTFOLIO_SECRET_CODE:
                messages.error(request, "Incorrect secret code. Experience was not deleted.")
                return redirect("main:show_experience")
            
            experience.delete()
            messages.success(request, "Experience deleted successfully.")
            return redirect("main:show_experience")
        return redirect("main:show_experience")

