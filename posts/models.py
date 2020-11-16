from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(
        "posts.Group", on_delete=models.SET_NULL, related_name="posts",
        blank=True, null=True
    )
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return f"{self.author}: {self.group}"
