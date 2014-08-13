from django.contrib import admin
from linguistic.models import *

class BiGramAdmin(admin.ModelAdmin):
    pass

class TriGramAdmin(admin.ModelAdmin):
    pass

class CompletionCacheAdmin(admin.ModelAdmin):
    pass
class WordListAdmin(admin.ModelAdmin):
    search_fields = ['word']

class SpellCorrectorAdmin(admin.ModelAdmin):
    pass
class GrammarAdmin(admin.ModelAdmin):
    pass
admin.site.register(BiGram,BiGramAdmin)
admin.site.register(TriGram, TriGramAdmin)
admin.site.register(CompletionCache,CompletionCacheAdmin)
admin.site.register(Word,WordListAdmin)
admin.site.register(SpellCache,SpellCorrectorAdmin)
admin.site.register(Grammar,GrammarAdmin)
