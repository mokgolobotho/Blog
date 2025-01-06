from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from .models import Blog, Comment

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
    # blogs = Blog.objects.all()
    blogs = Blog.objects.prefetch_related('comments').all()
    return render(request, "home.html", {'blogs': blogs})

def createAblog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("BlogApp:home")
    return render(request, "createAblog.html", {})

def myBlogs(request):
    blogs = Blog.objects.filter(user = request.user)
    return render(request, "myBlogs.html", {'blogs': blogs})

def edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("BlogApp:home")
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("BlogApp:home")

def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        comment_text = request.POST.get('comment')
        Comment.objects.create(blog=blog, comment=comment_text, user=request.user)
        return redirect('BlogApp:home')