from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def authView(request):
    print("debug1")
    if request.method == "POST":
        print("debug2 ")
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
