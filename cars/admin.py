from django.contrib import admin

from cars.models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30"  style="border-radius: 20%;" />', object.car_photo.url)

    thumbnail.short_description = 'Photo'
    list_display = ( 'car_title', 'thumbnail','state', 'city', 'color',   'is_featured')
    list_display_links = ('car_title', )
    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)