from django.shortcuts import render  # Модуль для имортирования (рендера?) html5 шаблонов.
from django.http import HttpResponse, HttpRequest
from .models import Post, Tag


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})  # render - функция отвечающая за рендер.
    '''Первый аргумент - обязательный (кухня веб-запросов)
    Второй - папка с шаблоном/название шаблона
    Третий - ожидает получение словаря, ключ - 'name', значение - переменная n, которая будет использована 
    Грубо говоря, КЛЮЧ словаря context - это все те переменные, которые мы будем передавать в шаблон.'''


def post_detail(request, slug):  # Арг. - обязат. requset и мы ждем что нам придет slug.
    # Теперь получаем из базы данных с помощью slug нужный пост.
    # iexact - грубо говоря slug равен переменной, которую мы получили во втором параметре функции.
    # slug попадая в функцию становится локальной переменной, которую мы и используем.
    post = Post.objects.get(slug__iexact=slug)
    # Теперь "отвечаем рендером"
    return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all() # Обращаемся к менеджеру модели Tag и получаем все теги.
    return render(request, 'blog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})