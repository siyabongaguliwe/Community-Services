from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Service, Event, Review

class ServiceEventReviewAPITestCase(APITestCase):
    def setUp(self):
        # Users
        self.provider = User.objects.create_user(username='provider', password='provpass')
        self.organizer = User.objects.create_user(username='organizer', password='orgpass')
        self.user = User.objects.create_user(username='user', password='userpass')
        self.other = User.objects.create_user(username='other', password='otherpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')

        # Tokens
        self.provider_token = Token.objects.create(user=self.provider)
        self.organizer_token = Token.objects.create(user=self.organizer)
        self.user_token = Token.objects.create(user=self.user)
        self.other_token = Token.objects.create(user=self.other)
        self.admin_token = Token.objects.create(user=self.admin)

        # Create a Service and Event to use in tests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.provider_token.key)
        service_resp = self.client.post('/api/services/', {
            'name': 'Plumbing',
            'category': 'Home',
            'description': 'Fixes pipes',
            'provider': self.provider.id
        }, format='json')
        self.assertEqual(service_resp.status_code, status.HTTP_201_CREATED)
        self.service_id = service_resp.data['id']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.organizer_token.key)
        event_resp = self.client.post('/api/events/', {
            'title': 'Community Meeting',
            'date': '2025-11-01',
            'location': 'Hall 1',
            'organizer': self.organizer.id,
            'details': 'Discuss issues'
        }, format='json')
        self.assertEqual(event_resp.status_code, status.HTTP_201_CREATED)
        self.event_id = event_resp.data['id']

    def test_service_post_put_delete(self):
        # Provider can update their service
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.provider_token.key)
        put_resp = self.client.put(f'/api/services/{self.service_id}/', {
            'name': 'Plumbing Pro',
            'category': 'Home',
            'description': 'All pipe work',
            'provider': self.provider.id
        }, format='json')
        self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(put_resp.data['name'], 'Plumbing Pro')

        # Other user cannot delete provider's service
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.other_token.key)
        del_resp = self.client.delete(f'/api/services/{self.service_id}/')
        self.assertEqual(del_resp.status_code, status.HTTP_403_FORBIDDEN)

        # Admin can delete
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        del_resp2 = self.client.delete(f'/api/services/{self.service_id}/')
        self.assertIn(del_resp2.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))

    def test_event_post_put_delete(self):
        # Organizer update
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.organizer_token.key)
        put_resp = self.client.put(f'/api/events/{self.event_id}/', {
            'title': 'Community Forum',
            'date': '2025-11-01',
            'location': 'Hall 1',
            'organizer': self.organizer.id,
            'details': 'Agenda updated'
        }, format='json')
        self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(put_resp.data['title'], 'Community Forum')

        # Other cannot delete
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.other_token.key)
        del_resp = self.client.delete(f'/api/events/{self.event_id}/')
        self.assertEqual(del_resp.status_code, status.HTTP_403_FORBIDDEN)

        # Admin can delete
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        del_resp2 = self.client.delete(f'/api/events/{self.event_id}/')
        self.assertIn(del_resp2.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))

    def test_review_post_duplicate_and_edge_cases(self):
        # Post a review
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        resp = self.client.post('/api/reviews/', {
            'user': self.user.id,
            'service': self.service_id,
            'rating': 5,
            'comment': 'Excellent'
        }, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # Duplicate review by same user for same service should fail (unique_together)
        resp2 = self.client.post('/api/reviews/', {
            'user': self.user.id,
            'service': self.service_id,
            'rating': 4,
            'comment': 'Good'
        }, format='json')
        self.assertIn(resp2.status_code, (status.HTTP_400_BAD_REQUEST, status.HTTP_409_CONFLICT))

        # Missing fields
        resp3 = self.client.post('/api/reviews/', {
            'user': self.user.id,
            # missing service
            'rating': 3,
            'comment': 'Ok'
        }, format='json')
        self.assertEqual(resp3.status_code, status.HTTP_400_BAD_REQUEST)

        # Invalid token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'invalidtoken')
        resp4 = self.client.post('/api/reviews/', {
            'user': self.user.id,
            'service': self.service_id,
            'rating': 2,
            'comment': 'Not good'
        }, format='json')
        self.assertIn(resp4.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))
