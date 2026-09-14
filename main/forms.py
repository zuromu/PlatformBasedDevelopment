from django import forms
from django.forms import TextInput, Textarea, Select, URLInput, DateTimeInput
from main.models import Experience

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