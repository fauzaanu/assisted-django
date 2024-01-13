from django.views import generic
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