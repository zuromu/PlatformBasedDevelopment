from django.urls import path

from main.views import (show_main, show_experience, show_projects, get_experience_json, delete_experience, update_experience, 
update_project, delete_project, get_projects_json, register, login_user, logout_user, toggle_star_project, toggle_star_experience,
create_project_ajax, create_experience_ajax, edit_project_ajax, edit_experience_ajax)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/<uuid:experience_id>/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/<uuid:id>/edit/", update_project, name="update_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star_project, name="toggle_star_project"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    path('edit-project-ajax/<uuid:id>/', edit_project_ajax, name='edit_project_ajax'),
    path('edit-experience-ajax/<uuid:id>/', edit_experience_ajax, name='edit_experience_ajax'),
    
    
]