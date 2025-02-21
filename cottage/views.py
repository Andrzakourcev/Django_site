from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request): #переменная request - ссылка на класс HttpRequest, которая содежит информацию о запросе
    return render(request, 'cottage/index.html')

def about(request):
    return render(request, 'cottage/about.html')
def parts(request, part_id):
    return HttpResponse(f"<h1>Части коттеджа</h1><p>id: {part_id}</p>")

def parts_by_slug(request, part_slug):
    return HttpResponse(f"<h1>Части коттеджа</h1><p>slug: {part_slug}</p>")

def arhive(request, year):
    # if request.GET:
    #     print('|'.join([f"{key}={value}" for key, value in request.GET.dict().items()]))
    if year <= 1900:
        uri = reverse('home') #reverse принимает name или название ф-и представления, url не принимает. Ф-я формирует маршрут для redirect'а
        return redirect(uri, permanent=True) #перенапрявляет с кодом 301 при True, с кодом 302 при false, также можно юзать HttpResponseRedirect и HttpResponsePermanentRedirect
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")