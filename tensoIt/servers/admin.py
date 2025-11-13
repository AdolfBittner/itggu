from django.contrib import admin
from .models import Server, VirtualServer

@admin.register(Server)
class AdminServer(admin.ModelAdmin):
    list_display = ['name','ipadr','description','hardware','yearstart','inwork']
    ordering = ['name']


@admin.register(VirtualServer)
class AdminVirtualServer(admin.ModelAdmin):
    list_display = ['name','ipadr','hardServer','description','virthardware','inwork','comment']
    list_filter = ('hardServer','inwork')
    ordering = ['hardServer']
    search_fields = ('name', 'ipadr','description', )
