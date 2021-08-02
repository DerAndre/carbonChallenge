import pytz
from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from usage.models import Usage, UsageType
from usage.management.commands import init_usage_types


class UsageTestCase(TestCase):
    """Includes all tests related to usage viewset"""

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin", password="superAdmin!")
        self.user = User.objects.create_user(
            username="user", password="normalUser!")
        self.usage_type = UsageType.objects.create(
            name="test_type", unit="kg", factor=1.0)
        self.client = APIClient()
        self.USAGE_TIME = '2021-08-01T15:30'

    def _create_usage(self):
        return Usage.objects.create(
            user=self.admin,
            usage_type=self.usage_type,
            usage_at=datetime.now(tz=pytz.UTC),
            amount=10
        )

    def test_create_usage_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(
            '/api/usage/',
            {
                'user': self.admin.pk,
                'usage_type': self.usage_type.pk,
                'amount': 5,
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_create_usage_fail_unauthorized(self):
        response = self.client.post(
            '/api/usage/',
            {
                'user': self.admin.pk,
                'usage_type': self.usage_type.pk,
                'amount': 5,
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_retrieve_usage_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(
            f'/api/usage/{self._create_usage().pk}/',
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_list_usage_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(
            f'/api/usage/{self._create_usage().pk}/',
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_put_usage_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(
            f'/api/usage/{self._create_usage().pk}/',
            {
                "usage_type": self.usage_type.pk,
                "user": self.admin.pk,
                "amount": 33,
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_put_usage_fail_invalid_data(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(
            f'/api/usage/{self._create_usage().pk}/',
            {
                "usage_type": self.usage_type.pk,
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 400)

    def test_put_usage_fail_object_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            f'/api/usage/{self._create_usage().pk}/',
            {
                "usage_type": self.usage_type.pk,
                "user": self.admin.pk,
                "amount": 33,
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 404)

    def test_patch_usage_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            f'/api/usage/{self._create_usage().pk}/',
            {
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_patch_usage_fail_object_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            f'/api/usage/{self._create_usage().pk}/',
            {
                'usage_at': self.USAGE_TIME
            },
            format='json'
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_usage_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(
            f'/api/usage/{self._create_usage().pk}/',
            format='json'
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_usage_fail_no_object_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            f'/api/usage/{self._create_usage().pk}/',
            format='json'
        )
        self.assertEqual(response.status_code, 404)


class UsageTypeTestCase(TestCase):
    """Includes all tests related to usage viewset"""

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin", password="superAdmin!")
        self.user = User.objects.create_user(
            username="user", password="normalUser!")
        self.client = APIClient()

    @staticmethod
    def _create_usage():
        return UsageType.objects.create(
            name='usage test type',
            unit='sm',
            factor=501
        )

    def test_create_usage_type_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(
            '/api/usage_type/',
            {
                'name': 'usage test type',
                'unit': 'sm',
                'factor': 501
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_create_usage_type_fail_forbidden(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/api/usage_type/',
            {
                'name': 'usage test type',
                'unit': 'sm',
                'factor': 501
            },
            format='json'
        )
        self.assertEqual(response.status_code, 403)

    def test_retrieve_usage_type_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            f'/api/usage_type/{self._create_usage().pk}/',
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_list_usage_type_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/api/usage_type/',
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_put_usage_type_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(
            f'/api/usage_type/{self._create_usage().pk}/',
            {
                'name': 'other test type',
                'unit': 'l',
                'factor': 105
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_patch_usage_type_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            f'/api/usage_type/{self._create_usage().pk}/',
            {
                'unit': 'bar',
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_usage_type_success(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(
            f'/api/usage_type/{self._create_usage().pk}/',
            {
                'unit': 'bar',
            },
            format='json'
        )
        self.assertEqual(response.status_code, 204)


class ManagementCommandsTestCase(TestCase):
    """Includes all tests for management commands"""

    def test_init_usage_types_command(self):
        init_usage_types.Command().handle()
        self.assertEqual(UsageType.objects.count(), 5)
