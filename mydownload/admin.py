from django.contrib import admin

# Register your models here.
from .models import *

class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)

class FenleiAdmin(admin.ModelAdmin):
    list_display = ('name',)

class WenZhangAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)

class FilesAdmin(admin.ModelAdmin):
    list_display = ('fileName', 'fileName',)

admin.site.register(Home, HomeAdmin)
admin.site.register(Fenlei, FenleiAdmin)
admin.site.register(WenZhang, WenZhangAdmin)
admin.site.register(Files, FilesAdmin)

