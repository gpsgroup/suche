from django.contrib import admin
from indexer.models import SucheURL

class SucheURLAdmin(admin.ModelAdmin):
    list_display = ['url']
admin.site.register(SucheURL,SucheURLAdmin)

