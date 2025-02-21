
from django.urls import path, re_path, register_converter
from . import converters
from . import views

register_converter(converters.FourDigitsConverter, "year4")


urlpatterns = [
    path('', views.index),
    path('parts/<int:part_id>/', views.parts),
    path('parts/<slug:part_slug>/', views.parts_by_slug),
    path('arhive/<year4:year>/', views.arhive)
]
