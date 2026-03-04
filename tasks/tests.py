from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class TaskTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="1234")

    def test_create_task(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post('/api/tasks/', {
            "title": "Test Task",
            "completed": False
        })

        self.assertEqual(response.status_code, 201)