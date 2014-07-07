from django.contrib import admin
from crawler.models import Rawdata,CrawlData

class RawDataAdmin(admin.ModelAdmin):
    list_display = ['url','operated']

admin.site.register(Rawdata,RawDataAdmin)



class CrawlDataAdmin(admin.ModelAdmin):
    list_display = ['url','uptodate']

admin.site.register(CrawlData,CrawlDataAdmin)
