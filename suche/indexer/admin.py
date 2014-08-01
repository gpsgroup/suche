from django.contrib import admin
from indexer.models import SucheURL,Link

class SucheURLAdmin(admin.ModelAdmin):
    list_display = ['url']

class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(SucheURL,SucheURLAdmin)
admin.site.register(Link,LinkAdmin)

