from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login_view"),
    path("register/", register_view, name="register_view"),
    path("add_blog/", add_blog, name="add_blog"),
    path("blog_detail/<slug>", blog_detail, name="blog_detail"),
    path("see_blog/", see_blog, name="see_blog"),
    path("blog_delete/<id>", blog_delete, name="blog_delete"),
    path("blog_update/<slug>", blog_update, name="blog_update"),
    path("logout_view/", logout_view, name="logout_view"),
    path("verify/<token>/", verify, name="verify"),

    


    

]
