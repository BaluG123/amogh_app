from django.contrib import admin
from . models import Apps

class AppAdmin(admin.ModelAdmin):
    list_display=['no','appname','logo','category','home_description','steps','detail_description','andriod_link','andriod_rate','total_andownloads','total_iosdownloads','ios_link','ios_rate','publish']
    list_filter=('appname','publish')
    search_fields=('appname','home_description','detail_description')
    prepopulated_fields={'slug':('appname',)}

# Register your models here.
admin.site.register(Apps,AppAdmin)