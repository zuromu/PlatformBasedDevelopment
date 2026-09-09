from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.html import escape

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Mentor for Open House Fasilkom UI 2025",
            description="Guided prospective students through the CS/IS programs, explaining curriculum details, campus culture, and the university environment.",
            category="volunteer",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Mentor for Open House Fasilkom UI 2025")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Volunteer")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Wanderer's Koperasi Quest",
            tech_stack="JavaScript, HTML, CSS, Phaser",
            description="RPG Edukasi Keuangan yang mengajarkan konsep koperasi Indonesia lewat petualangan.",
            github_url="https://github.com/zuromu/Wanderers-Koperasi"
        )

    def test_project_model(self):
        self.assertEqual(str(self.project), "Wanderer's Koperasi Quest")
        self.assertEqual(self.project.tech_stack, "JavaScript, HTML, CSS, Phaser")

    def test_projects_page_is_accessible_and_renders_data(self):
        response = self.client.get(reverse("main:show_projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, escape("Wanderer's Koperasi Quest"))
        self.assertContains(response, "JavaScript, HTML, CSS, Phaser")
        self.assertContains(response, "RPG Edukasi Keuangan yang mengajarkan konsep koperasi Indonesia lewat petualangan.")
        self.assertContains(response, "https://github.com/zuromu/Wanderers-Koperasi")
        
    def test_empty_projects_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))
        self.assertContains(response, "No projects have been added yet.")