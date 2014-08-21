from django.contrib import admin
from pluginServer.models import Wordmeaning
# Register your models here.
class Wordmeaningadmin(admin.ModelAdmin):
    pass
admin.site.register(Wordmeaning,Wordmeaningadmin)