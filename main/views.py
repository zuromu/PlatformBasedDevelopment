import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.forms import ExperienceForm, ProjectForm
from main.models import Experience, Project

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Ahmad Hoesin",
        "npm": "25065&#8203;55400",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and DevOps."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

#Experience
@login_required(login_url="/login/")
def add_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New Experience Added!")
        return redirect("main:show_experience")

    context = {"name": "Ahmad Hoesin", "form": form}
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated successfully!")
        return redirect("main:show_experience")

    context = {"name": "Ahmad Hoesin", "form": form, "experience": experience}
    return render(request, "experience_form.html", context)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Ahmad Hoesin",
        "title_query": title_query,
        "is_editor": is_editor(request.user),
        "form": ExperienceForm(), 
    }
    return render(request, "experience.html", context)



def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for exp in experiences:
        starred_users = exp.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "category": exp.category,
                "thumbnail": exp.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": ", ".join([u.username for u in starred_users]),
            }
        })
    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted successfully.")
        return redirect("main:show_experience")
    return redirect("main:show_experience")


#Projects
@login_required(login_url="/login/")
def update_project(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project successfully updated!")
        return redirect("main:show_projects")
    
    context = {"form": form, "name": "Ahmad Hoesin", "project": project}
    return render(request, "project_form.html", context)

@login_required(login_url="/login/")
def delete_project(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
        
    project = get_object_or_404(Project, pk=id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")
    return redirect("main:show_projects")

def get_projects_json(request):
    name_query = request.GET.get("name", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if name_query:
        projects = projects.filter(title__icontains=name_query)

    # Manually build the JSON data so we can add the Star logic
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "name": project.name,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "github_url": project.github_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


def show_projects(request):
    name_query = request.GET.get("name", "").strip()

    context = {
        "name": "Ahmad Hoesin",
        "name_query": name_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)

#Auth
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Ahmad Hoesin",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Ahmad Hoesin",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

#star
@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
    return redirect("main:show_experience")



#Editor
def is_editor(user):
    return user.is_authenticated and user.groups.filter(name__iexact="editor").exists()

#ajax
@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_experience_ajax(request):
    # Only superusers can add experience
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience added successfully.", "pk": str(experience.id)},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)