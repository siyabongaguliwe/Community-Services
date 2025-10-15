from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Listing

class ListingPermissionTestCase(APITestCase):
    def setUp(self):
        # Create users
        self.owner = User.objects.create_user(username='owner', password='ownerpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')

        # Create tokens
        self.owner_token = Token.objects.create(user=self.owner)
        self.other_token = Token.objects.create(user=self.other_user)
        self.admin_token = Token.objects.create(user=self.admin)

        # Create a Listing owned by 'owner'
        self.listing = Listing.objects.create(
            title='Affordable Room',
            description='Clean and cozy',
            price=500.00,
            location='Polokwane',
            owner=self.owner
        )

    def test_owner_can_access(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.owner_token.key)
        response = self.client.get(f'/api/listings/{self.listing.id}/')
        self.assertEqual(response.status_code, 200)

    def test_other_user_denied(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.other_token.key)
        response = self.client.get(f'/api/listings/{self.listing.id}/')
        self.assertEqual(response.status_code, 403)

    def test_admin_can_access(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        response = self.client.get(f'/api/listings/{self.listing.id}/')
        self.assertEqual(response.status_code, 200)
