from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedView, LikePostView
from django.urls import path
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
path('posts/<int:pk>/like', LikePostView.as_view()),
path('posts/<int:pk>/unlike/', LikePostView.as_view()),


urlpatterns = router.urls
urlpatterns += [
    path('feed/', FeedView.as_view(), name='feed'),]
