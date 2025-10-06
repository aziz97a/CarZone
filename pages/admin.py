from django.contrib import admin

from pages.models import team
from django.utils.html import format_html
# Register your models here.
class teamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30"  style="border-radius: 20%;" />', object.photo.url)

    thumbnail.short_description = 'Photo'

    list_display = ('id','first_name', 'thumbnail', 'designation', 'created_date')
    list_display_links = ('first_name', )
    search_fields = ('first_name','last_name', 'designation')
    list_filter = ('designation',)
    
admin.site.register(team,teamAdmin)
