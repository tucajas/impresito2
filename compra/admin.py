from django.contrib import admin
from .models import Proveedor,MateriaPrima,Compra

admin.site.register(Proveedor)
admin.site.register(MateriaPrima)
admin.site.register(Compra)