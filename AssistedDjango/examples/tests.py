from django.test import TestCase
from .models import Post, Category

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Sample Category')
        Post.objects.create(title='Test title', content='Test content', category=Category.objects.get(id=1))

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_content_is_required(self):
        post = Post.objects.get(id=1)
        field = post._meta.get_field('content')
        self.assertFalse(field.null)

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Sample Category')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)