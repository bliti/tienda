from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.core.urlresolvers import reverse


class LadingPageTest(TestCase):
    """
    Note: You should go ahead and do your own integration tests
    with selenium or something like it.
    This merely makes sure the landing page runs.
    It does not test style or layout.
    """
    def setUp(self):
        self.client = Client()
    
    
    def test_landing_page_request_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    
    def test_company_name_in_landing_page(self):
        response = self.client.get(reverse('index'))
        self.assertTrue(settings.COMPANY_NAME in response.content)