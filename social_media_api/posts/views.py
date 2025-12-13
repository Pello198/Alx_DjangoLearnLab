
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from notifications.models import Notification




class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the list of users the current user is following
        following_users = request.user.following.all()

        # Fetch posts by those users, ordered by creation date (most recent first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)



class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # ALX-required line to fetch the post
        post = generics.get_object_or_404(Post, pk=pk)

        # ALX-required line to like the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)


