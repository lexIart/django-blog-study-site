from django.shortcuts import render, get_object_or_404, redirect, reverse  # Модуль для имортирования (рендера?) html5 шаблонов.
from django.views.generic import View
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.core.exceptions import ValidationError
# CRUD model?


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})  # render - функция отвечающая за рендер.
    '''Первый аргумент - обязательный (кухня веб-запросов)
    Второй - папка с шаблоном/название шаблона
    Третий - ожидает получение словаря, ключ - 'name', значение - переменная n, которая будет использована 
    Грубо говоря, КЛЮЧ словаря context - это все те переменные, которые мы будем передавать в шаблон.'''


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):  # tag creating view.
    form_model = TagForm
    template = 'blog/tag_create.html'

    # def get(self, request):  # response method to "get" request.
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    #
    # def post(self, request):  # response method to "post" request.
    #     bound_form = TagForm(request.POST)
    #
    # # here we are realizing creating logic of tags.
    # # first of all we checking entered data on validness to avoid injections/empty fields and other.
    # # if all good we saving new tag and return
    #     if bound_form.is_valid() == True:
    #         new_tag = bound_form.save()
    #         # and redirecting user to URL of created tag.
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})

class TagUpdate(ObjectUpdateMixin, View):  # updating an existing element (model) of a project by a user in this method.
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    # def get(self, request, slug):  # getting object.
    #     tag = Tag.objects.get(slug__iexact=slug)  # identify object (tag in this situation) as a slug.
    #     bound_form = TagForm(instance=tag)  # taking an object from DB, creating bound form.
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'

def tags_list(request):
    tags = Tag.objects.all() # Обращаемся к менеджеру модели Tag и получаем все теги.
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    #
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form': bound_form})


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'


class PostDetail(ObjectDetailMixin, View):  # creating class for refactoring same methods with some inheritance.
    model = Post
    template = 'blog/post_detail.html'

