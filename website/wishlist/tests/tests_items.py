from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from wishlist.views import item_list_admin


class TestItemsAdmin(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='top_secret', is_superuser=True)

    def test_list(self):
        request = self.factory.get('/admin/wishlist/item/list')
        request.user = self.user
        response = item_list_admin(request)
        self.assertEqual(response.status_code, 200)