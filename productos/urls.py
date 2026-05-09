from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home_productos'),
    path('logins',views.login, name='logins'),
    path('cervezas',views.lista_cervezas, name='cervezas'),
]