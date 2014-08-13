from django.contrib import admin
from plugin.models import *
# Register your models here.
class PluginAdmin(admin.ModelAdmin):
    pass
class GrammarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plugin,PluginAdmin)
admin.site.register(Grammar,GrammarAdmin)