from django.contrib import admin
from .models import Producto
from .models import Cerveza

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cerveza)
class ProductoAdmin(admin.ModelAdmin):
    pass