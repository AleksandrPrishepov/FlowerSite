from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug','description', 'get_html_photo', 'time_create', 'time_update','is_published', 'cat')
    list_display_links = ('id', 'name', 'slug')
    search_fields = ('name', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug':('name',)}
    fields = ('name', 'slug','description', 'is_published', 'cat', 'get_html_photo', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_description = 'Миниатюра'

    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'n_cat', 'slug')
    list_display_links = ('id', 'n_cat')
    search_fields = ('n_cat',)
    prepopulated_fields = {'slug': ('n_cat',)}

admin.site.register(Flower, FlowerAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ сайта о цветах'
admin.site.site_header = 'Администрирование сайта о цветах'
