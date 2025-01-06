from django.urls import path, include
from .views import authView,home, createAblog, myBlogs, edit_blog, delete_blog, add_comment
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("createAblog/", createAblog, name="createAblog"),
    path("myBlogs/", myBlogs, name="myBlogs"),
    path('logout/', LogoutView.as_view(next_page='BlogApp:home'), name='logout'),
    path('edit/<int:id>/', edit_blog, name='edit_blog'),
    path('delete/<int:id>/', delete_blog, name='delete_blog'),
    path('add-comment/<int:blog_id>/', add_comment, name='addComment'),

] 