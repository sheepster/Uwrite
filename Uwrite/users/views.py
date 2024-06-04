from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib import messages
from .forms import ProfileForm



def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:main")
        else:
            context = {"form": form}
            return render(request, "users/register.html", context)
    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)

def author_profile(request, id):
    author = User.object.get(id=id)

    context = {
        'author': author
    }
    return render (request, 'user/userprofile.html', context)

@login_required
def profile(request):
    return render(request, "users/profile.html")




# Create your views here.
