from django.http import HttpResponse
from django.shortcuts import render

def index(requests): #переменная requests - ссылка на класс HttpRequest, которая содежит информацию о запросе
    return HttpResponse("Страница приложения cottage")


def parts(requests, part_id):
    return HttpResponse(f"<h1>Части коттеджа</h1><p>id: {part_id}</p>")

def parts_by_slug(requests, part_slug):
    return HttpResponse(f"<h1>Части коттеджа</h1><p>slug: {part_slug}</p>")

def arhive(requests, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")