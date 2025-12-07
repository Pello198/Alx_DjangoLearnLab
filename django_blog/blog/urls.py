# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    # Registration & profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Login & logout using built-in views with custom templates
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts-by-tag'),


]
