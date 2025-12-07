# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']   # oldest first; change to ['-created_at'] if you prefer newest first

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    def get_absolute_url(self):
        # After edit/delete/create we return to the post detail page
        return reverse('post-detail', kwargs={'pk': self.post.pk})
    
    
# Optional: profile extension
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # avatar requires Pillow; store uploaded files under MEDIA_ROOT
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

# Create/update Profile when a User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
