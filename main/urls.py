from django.urls import path

from main.views import (show_main, show_experience, show_projects, add_experience, get_experience_json, delete_experience, 
update_experience, create_project, update_project, delete_project, get_projects_json)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/<uuid:experience_id>/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/add/", add_experience, name="add_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:id>/edit/", update_project, name="update_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    
]