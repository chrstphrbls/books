# # pages/tests.py
# from typing_extensions import Self
# from urllib import response
# from django.test import SimpleTestCase
# from django.urls import reverse

# class HomepageTests(SimpleTestCase):
#     def test_homepage_status(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code,200)

#     def test_homepage_url_name(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code,200)

#     def test_homepage_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response,'home.html')

#     def test_homepage_contains_correct_html(self):
#         response = self.client.get('/')
#         self.assertContains(response,'Homepage')

#     def test_homepage_does_not_contain_incorrect_html(self):
#         response = self.client.get('/')
#         self.assertNotContains(
#             response, 'Hie there! I should not be on the page.'
#         )

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response,'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response,'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response,'Hi there! I should not be on the page.'
        )
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


