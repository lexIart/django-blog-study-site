from django.http import HttpResponse  #


def hello(request):  # Все функции обработчики принимают обязательный аргумент requset
    return HttpResponse('<h1>Я обработал функцию hello и возвращаю ответ это сигнализирующий!</h1>')

