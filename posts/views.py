from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    return render(request, "index.html", {"posts": posts})


def group_posts(request, group_slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных
    # или возвращает сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=group_slug)
    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}

    posts = group.posts.all().order_by('-pub_date')[:12]
    context = {"group": group, "posts": posts}
    return render(request, "group.html", context)
