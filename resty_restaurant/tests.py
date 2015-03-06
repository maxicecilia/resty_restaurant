from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Venue


class VenuTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='tester@resty.com',
            username='tester@resty.com',
            password='dont_look_at_me'
        )
        self.get_url = reverse('venue-list')
        self.venue_mock_data = {
            'name': 'test_name', 'address': 'test_address', 'stars': 1,
            'cellphone': '555444333', 'landline': '555444222'
        }

    def test_venue_list_empty(self):
        """ """
        response = self.client.get(self.get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_venue_list_not_empty(self):
        """ """
        test_venue = self._create_venue()
        response = self.client.get(self.get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        test_venue.delete()

    def test_venue_detail_not_found(self):
        response = self.client.get('{}1/'.format(self.get_url), format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], u'Not found')

    def test_venue_detail_found(self):
        test_venue = self._create_venue()
        response = self.client.get('{0}{1}/'.format(self.get_url, test_venue.pk), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data), 0)

    def test_venue_create_ok(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('{}'.format(self.get_url), self.venue_mock_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.venue_mock_data['name'])
        self.assertEqual(response.data['address'], self.venue_mock_data['address'])

    def _create_venue(self):
        venue = Venue(**self.venue_mock_data)
        venue.save()
        return venue
