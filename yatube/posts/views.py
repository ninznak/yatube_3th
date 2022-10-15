from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)

def name(request):
    return HttpResponse('<h1 style="color: red; font-size: 45px; margin: 20%;">Привет <i><b>путник!</b></i>')

def yandex(request):
    return HttpResponse("<a href='https://yandex.ru/'>Ссылка на <b>Яндекс</b></a>")