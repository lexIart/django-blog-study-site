from django.db import models
from django.shortcuts import reverse  # Генерация ссылок?
"""Post - модель постов блога."""


class Post(models.Model):
    # Определяем заголовок нашей модели постов.
    # title - экземпляр класса Charfield.
    # обязательный параметр max_length, значение 150.
    # Обеспечиваем индексацию параметром db_index=True для более быстрого поиска.
    title = models.CharField(max_length=150, db_index=True)
    # Определим ЧПУ через экз. класса SlugField для ясности использования адресов.
    # Поля параметром unique=True автоматически индексируются, поэтому здесь db_index явно не указан.
    slug = models.SlugField(max_length=150, unique=True)
    # Определим содержимое поста (тело), разрешим делать его пустым.
    body = models.TextField(blank=True, db_index=True)
    # Единственный параметр auto_now_add указывает на автоматическое заполнение поля publication_date при сохр. в БД.
    publication_date = models.DateTimeField(auto_now_add=True)
    # В параметрах экземпляра класса указываем класс, с которым мы хотим установить связь ManyToMany.
    # Так же создадим обратную связь между экземплярами классов Post и Tag.
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):  # URL reversing.
        """К этой функции python мы будем обращаться из html, дабы немного оптимизировать код.
        на больших проектах во избежания путаницы. Данная функция автоматически генерирует необходимый.
        html код, чтобы нам осталось лишь явно указать на функцию get_absolute_url класса Post.
        чтобы вставить ссылку на какой-либо элемет (будь то кнопка или гиперссылка) явно."""
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    # Определям метод модели (класса).
    def __str__(self):
        # *Переопределяем метод стринг для наглядности вывода информации об объекте.
        return '{}'.format(self.title)
    # После всех необходимых корректировок и изменений модели необходимо произвести миграцию базы данных.
    # makemigrations - migrate (применить).


class Tag(models.Model):  # Модель тегов для блога.
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
