# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment
from taggit.forms import TagWidget



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 10}),
            'tags': TagWidget(),
        }
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...', 'class': 'form-control'}),
        max_length=2000
    )

    class Meta:
        model = Comment
        fields = ['content']
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
