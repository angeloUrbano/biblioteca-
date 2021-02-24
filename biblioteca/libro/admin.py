from django.contrib import admin
from libro.models import Libro , Autor , reservation
# Register your models here.



admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(reservation)
