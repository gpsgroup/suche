from django.contrib import admin
from crawler.models import Rawdata,CrawlData

class RawDataAdmin(admin.ModelAdmin):
    list_display = ['url','operated']
    

admin.site.register(Rawdata,RawDataAdmin)

class CrawlDataAdmin(admin.ModelAdmin):
    list_display = ['url','uptodate']
    search_fields = ['url__url']

admin.site.register(CrawlData,CrawlDataAdmin)
