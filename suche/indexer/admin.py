from django.contrib import admin
from indexer.models import SucheURL,Link,Word,Result

class SucheURLAdmin(admin.ModelAdmin):
    list_display = ['url']
    search_fields = ['url']


class LinkAdmin(admin.ModelAdmin):
    pass
class WordAdmin(admin.ModelAdmin):
    pass
class ResultAdmin(admin.ModelAdmin):
    list_display = ('word', 'url' , 'urlpoint')
    search_fields = ['word__word']
    
admin.site.register(SucheURL,SucheURLAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Word,WordAdmin)
admin.site.register(Result,ResultAdmin)

