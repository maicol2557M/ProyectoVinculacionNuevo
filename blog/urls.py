from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_Articulos, name='lista_articulos'),
]