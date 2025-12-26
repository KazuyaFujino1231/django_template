from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthEchoTests(APITestCase):
    def test_healthcheck_returns_ok(self):
        url = reverse('api-health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'status': 'ok'})

    def test_echo_returns_payload(self):
        url = reverse('api-echo')
        payload = {'message': 'hello'}
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'echo': payload})
