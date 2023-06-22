from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class BookingTest(APITestCase):
    def test_get_id(self):
        url = reverse('get_bookings', args=[2])
        response = self.client.get(url)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

###the reason is 401 because there's it should be unauthorized