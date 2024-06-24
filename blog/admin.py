from django.contrib import admin
from blog.models import Rasmlar,Matn,Ishchilar,Xodimlar


# Register your models here.


@admin.register(Rasmlar)
class RasmAdmin(admin.ModelAdmin):
    list_display = ['nomi']


@admin.register(Matn)
class MatnAdmin(admin.ModelAdmin):
    list_display = ['nomi']

# Register your models here.
@admin.register(Ishchilar)
class IshchilarAdmin(admin.ModelAdmin):
    list_display = ['ismi']

@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ['ismi']