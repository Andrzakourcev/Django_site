from django.http import HttpResponse
from django.shortcuts import render

def index(requests): #переменная requests - ссылка на класс HttpRequest, которая содежит информацию о запросе
    return HttpResponse("Страница приложения cottage")


def parts(requests):
    return HttpResponse("<h1>Части коттеджа</h1>")