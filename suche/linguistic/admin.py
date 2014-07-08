from django.contrib import admin
from linguistic.models import BiGram, TriGram, CompletionCache

class BiGramAdmin(admin.ModelAdmin):
    pass

class TriGramAdmin(admin.ModelAdmin):
    pass

class CompletionCacheAdmin(admin.ModelAdmin):
    pass

admin.site.register(BiGram,BiGramAdmin)
admin.site.register(TriGram, TriGramAdmin)
admin.site.register(CompletionCache,CompletionCacheAdmin)
