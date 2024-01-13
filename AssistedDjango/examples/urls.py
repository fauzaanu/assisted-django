from django.urls import path
from . import views

app_name = 'blog'  # application namespace
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>/', views.CategoryListView.as_view(), name='category_list'),
]