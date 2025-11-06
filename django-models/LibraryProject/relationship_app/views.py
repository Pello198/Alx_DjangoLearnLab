from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
    return user.userprofile.role == "Admin"

def check_librarian(user):
    return user.userprofile.role == "Librarian"

def check_member(user):
    return user.userprofile.role == "Member"

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, "admin_view.html")

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")

@user_passes_test(check_member)
def member_view(request):
    return render(request, "member_view.html")


# FUNCTION BASED VIEW
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# CLASS BASED VIEW
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')