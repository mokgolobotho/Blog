from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("BlogApp:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def home(request):
    return render(request, "home.html", {})

def createAblog(request):
    if request.method == "POST":
        return redirect("BlogApp:home")
    return render(request, "createAblog.html", {})
