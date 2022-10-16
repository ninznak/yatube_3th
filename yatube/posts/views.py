from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def index(request):    
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube :))'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title' : title,
        'text' : text,
        'posts' : posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title' : title,
        'text' : text,
    }
    return render(request, template, context)

def name(request):
    return HttpResponse('<h1 style="color: red; font-size: 45px; margin: 20%;">Привет <i><b>путник!</b></i>')

def yandex(request):
    return HttpResponse("<a href='https://yandex.ru/'>Ссылка на <b>Яндекс</b></a>")