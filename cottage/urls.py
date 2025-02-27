
from django.urls import path, re_path, register_converter
from . import converters
from . import views

register_converter(converters.FourDigitsConverter, "year4")


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    # path('parts/<int:part_id>/', views.parts, name='parts_int'),
    # path('parts/<slug:part_slug>/', views.parts_by_slug, name='parts_by_slug'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews'),
    path('arhive/<year4:year>/', views.arhive, name='arhive'),
    path('book/', views.book, name='book'),
    path('contacts/', views.contacts, name='contacts'),
]
