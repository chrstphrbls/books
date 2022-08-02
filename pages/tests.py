# pages/tests.html
from urllib import response
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve 

from .views import HomePageView, AboutPageView

class HompageTest(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response,'Hi there! I should not be on the page.'
        )

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )




    
