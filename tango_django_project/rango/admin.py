from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'category', 'views']

class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']    

admin.site.register(Category, CatAdmin)
admin.site.register(Page, PageAdmin)
