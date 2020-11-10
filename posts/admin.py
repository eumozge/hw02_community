from django.contrib import admin

from .models import Post, Group


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"
    list_select_related = ("author", "group")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "description")
    search_fields = ("slug", "title")
