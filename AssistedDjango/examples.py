ADMIN_EXAMPLE = """from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'author', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)      
  
# NOTES TO DEVELOPER:       
# [NOTE]       
# [NOTE]   
# [NOTE]   
# [NOTE]    
"""

FORMS_EXAMPLE = """from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Users, Posts, Comments, Replies

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['user_id', 'post_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user_id', 'comment_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class RepliesForm(forms.ModelForm):
    class Meta:
        model = Replies
        fields = ['user_id', 'reply_text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
 
             
# NOTES TO DEVELOPER:       
# You will need to install crispy_forms in your virtual environment.
# [NOTE]   
# [NOTE]   
# [NOTE]    
"""

TESTS_EXAMPLE = """from django.test import TestCase
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
        
        
# NOTES TO DEVELOPER:       
# [NOTE]       
# [NOTE]   
# [NOTE]   
# [NOTE]    
"""

URLS_EXAMPLE = """from django.urls import path
from . import views

app_name = 'blog'  # application namespace
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>/', views.CategoryListView.as_view(), name='category_list'),
]   
     
# NOTES TO DEVELOPER:       
# [NOTE]       
# [NOTE]   
# [NOTE]   
# [NOTE]    
"""

VIEWS_EXAMPLE = """from django.views import generic
from .models import Post, Category

class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'  # your template name
    context_object_name = 'posts'  # your variable name in the template

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'  # your template name

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'  # your template name
    context_object_name = 'categories'  # your variable name in the template
        
# NOTES TO DEVELOPER:       
# [NOTE]       
# [NOTE]   
# [NOTE]   
# [NOTE]    
"""

MODEL_EXAMPLE = """from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title    
            
# NOTES TO DEVELOPER:       
# [NOTE]       
# [NOTE]   
# [NOTE]   
# [NOTE]    
"""
