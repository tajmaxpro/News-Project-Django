from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='News title', text='news text')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expexted_object_title = f'{post.title}'
        expexted_object_text = f'{post.text}'
        self.assertEqual(expexted_object_title, 'News title')
        self.assertEqual(expexted_object_text, 'news text')

class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(title='News title 2', text='another news')

    def test_views_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        #self.assertEqual(resp, 'home.html')