from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.urls import reverse

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Забронировать', 'url_name': 'book'},
    {'title': 'Галерея', 'url_name': 'gallery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
    {'title': 'Контакты', 'url_name': 'contacts'},
    {'title': 'О сайте', 'url_name': 'about'},
]


def index(request):  # переменная request - ссылка на класс HttpRequest, которая содежит информацию о запросе
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'cottage/index.html', context=data)


def book(request):
    data = {
        'title': 'Забронировать',
        'menu': menu,
    }
    return render(request, 'cottage/book.html', context=data)


def gallery(request):
    data = {
        'title': 'Галерея',
        'menu': menu,
    }
    return render(request, 'cottage/gallery.html', context=data)


def contacts(request):
    data = {
        'title': 'Контакты',
        'menu': menu,
    }
    return render(request, 'cottage/contacts.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'cottage/about.html', context=data)


def reviews(request):
    data = {
        'title': 'Отзывы',
        'menu': menu,
    }
    return render(request, 'cottage/reviews.html', context=data)


# def parts(request, part_id):
#     return HttpResponse(f"<h1>Части коттеджа</h1><p>id: {part_id}</p>")
#
#
# def parts_by_slug(request, part_slug):
#     return HttpResponse(f"<h1>Части коттеджа</h1><p>slug: {part_slug}</p>")


def arhive(request, year):
    if year <= 1900:
        uri = reverse(
            'home')  # reverse принимает name или название ф-и представления, url не принимает. Ф-я формирует маршрут для redirect'а
        return redirect(uri,
                        permanent=True)  # перенапрявляет с кодом 301 при True, с кодом 302 при false, также можно юзать HttpResponseRedirect и HttpResponsePermanentRedirect
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
