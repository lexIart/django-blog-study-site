from django.urls import path
from .views import *  # Импортируем всё (функции и прочее-прочее)
"""'' - Определяем третий атрибут name для удобного использования в шаблонах
'post/str:slug' - Определяем именнованную группу символов для определния пути 
каждого поста (slug и помог), и определение __str__ для str символов адресов тоже использовалось.
'tags/' - Обозначаем функцию-обработчик как tags_list."""


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url')
]