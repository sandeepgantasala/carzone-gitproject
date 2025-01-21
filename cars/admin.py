from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

# class CarAdmin(admin.ModelAdmin):
#     #for thumbnail
#     def thumbnails(self,object):
#         return format_html('<img src="{}" width="40" style="border-radius:10px"/>'.format(object.car_photo.url))
    
#     thumbnails.short_description="Image"


#     #for showing in table
#     list_display=("id","thumbnails","car_title","city","color","model","year","body_style","fuel_type","is_featured")
#     list_display_links=("id","car_title","thumbnails")
#     search_fields=("car_title","city","model","year","body_style","fuel_type")
#     list_filter=("city","model","year","body_style")


class CarAdmin(admin.ModelAdmin):
    def thumbnails(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:10px"/>'.format(object.car_photo.url))
    
    thumbnails.short_description="Car Image"
    list_display=('id','thumbnails','car_title','color','model','year','city','body_style','fuel_type','is_featured')
    list_display_links=('id','thumbnails','car_title')
    list_filter=('color','city','model')
    list_editable=('is_featured',)
    search_fields=('model','city','color','fuel_type','body_style','car_title')
    

admin.site.register(Car,CarAdmin)
