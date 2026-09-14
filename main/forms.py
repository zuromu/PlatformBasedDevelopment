from django import forms
from django.forms import TextInput, Textarea, Select, URLInput
from main.models import Experience, Project

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Experience Title",
            "description": "Experience Description",
            "category": "Experience Category",
            "thumbnail": "Experience Thumbnail",
        }

        widgets = {

            "title": TextInput(
                attrs={
                    "placeholder": "Experience Title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Experience Description",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                    "placeholder": "Experience Category",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "Experience Thumbnail URL",
                }
            ),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "tech_stack",
            "description",
            "github_url",
        ]
        labels = {
            "name": "Project Name",
            "tech_stack": "Tech Stack",
            "description": "Description",
            "github_url": "GitHub Repository URL",
        }
        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "e.g., Wanderer's Koperasi Quest",
                    "maxlength": 255,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "e.g., JavaScript, HTML, CSS, Phaser",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe what you built...",
                    "rows": 4,
                }
            ),
            "github_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/zuromu/...",
                }
            ),
        }