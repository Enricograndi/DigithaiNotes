from django.test import TestCase
from django.contrib.messages import get_messages
from http import HTTPStatus
from django.contrib.auth import get_user_model
from .models import Notes

class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up test data for all the test methods in this test case.
        cls.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        cls.notes = Notes.objects.create(user=cls.user, title="This is a test!")

    def test_model_content(self):
        # Test the content of the 'Notes' model.
        self.assertEqual(self.notes.title, "This is a test!")

    def test_edit_content(self):
        # Test editing the content of the 'Notes' model.
        self.notes.title = "This is NOT a test!"
        self.notes.save()
        self.assertEqual(self.notes.title, "This is NOT a test!")

    def test_form_notes(self):
        # Test the form submission for creating notes.
        self.client.force_login(self.user)
        response = self.client.post("/create-notes", data={"title": "This is a test form"}, follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_form_notes_messages(self):
        # Test form submission for creating notes and check if the appropriate error message is shown.
        self.client.force_login(self.user)
        response = self.client.post("/create-notes", data={"title": "This is a test form"}, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertEquals(str(messages[0]), "Ops, something went wrong")

    def test_url_exists_at_correct_location(self):
        # Test if the URL to create notes exists and responds with a 200 status code.
        self.client.force_login(self.user)
        response = self.client.get("/create-notes")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_login(self):
        # Test if the URL to create notes redirects to the login page (status code 302) for anonymous users.
        response = self.client.get("/create-notes")
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

