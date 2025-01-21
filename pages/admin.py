from django.contrib import admin
from.models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):

   
   #for thumbnail
    def thumbnails(self,object):
        return format_html('<img src="{}" width="35" style="border-radius:20px"/>'.format(object.photo.url))
    
    thumbnails.short_description="Image"


    #for showing in table
    list_display=("id","thumbnails","first_name","last_name","designation","created_date")
    list_display_links=("id","first_name","thumbnails")
    search_fields=("first_name","last_name","designation")
    list_filter=("designation",)

admin.site.register(Team,TeamAdmin)