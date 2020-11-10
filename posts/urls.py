from django.urls import path

from .views import index, group_posts

urlpatterns = [
    path("", index, name="index"),
    path("group/<slug:group_slug>/", group_posts, name="group-posts")
]
