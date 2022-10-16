from django.shortcuts import render, get_object_or_404

from .models import Post, Group

from django.http import HttpResponse


def index(request):    
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube :))'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    
    context = {
        'group': group,
        'posts': posts,        
    }
    return render(request, 'posts/group_list.html', context)


def name(request):
    return HttpResponse('<h1 style="color: red; font-size: 45px; margin: 20%;">Привет <i><b>путник!</b></i>')


def yandex(request):
    return HttpResponse("<a href='https://yandex.ru/'>Ссылка на <b>Яндекс</b></a>")