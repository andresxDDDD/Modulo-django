from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto,Cerveza

# Create your views here.
def index(request):#ve a buscar los productos en la base de datos y pasaselos a index
  productos = Producto.objects.all() # asigna a la variable los productos desde la bd como objetos
  return render(request,'productos/home.html',{'productos': productos})# 

def lista_cervezas(request):
    cerveza= Cerveza.objects.all()  
    return render(request,'beer/beer.html',{'cerveza':cerveza})


def dashboard(request):
 return HttpResponse("dashboard")


def login(request):
 return HttpResponse("login")

def register(request):
 return HttpResponse("register")

def register(request):
 return HttpResponse("vender")