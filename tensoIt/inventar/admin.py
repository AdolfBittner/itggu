from django.contrib import admin
from .models import Computer, Printer, TensoMail, License, User1C, VNCuser, OxranaCam
from kadry.models import Polzovatel

admin.site.site_header = 'ГГУ Курсовой проект'

@admin.register(Computer)
class AdminComputer(admin.ModelAdmin):
    list_display=['inventarNum','SetevoeImya','Polzovatel','Konfiguracia', 'OS', 'Office', 'DataPokupki']
    search_fields = ('inventarNum','Polzovatel__name','Konfiguracia', 'OS', 'Office', 'DataPokupki','SetevoeImya')
    list_filter = ('DataPokupki','Podrazdelenie', 'OS', 'Office')


@admin.register(Printer)
class AdminPrinter(admin.ModelAdmin):
    list_display = ['PrintModel', 'TipPrint', 'SetPrint','Mesto', 'Kommentariy' ]
    search_fields = ('PrintModel', 'TipPrint', 'SetPrint','Mesto', 'Kommentariy')

@admin.register(TensoMail)
class AdminTensoMail(admin.ModelAdmin):
    list_display = ['MailAdr', 'MailPass', 'UserMail']
    search_fields = ('MailAdr', 'MailPass', 'UserMail__name')

@admin.register(License)
class AdminLicense(admin.ModelAdmin):
    list_display = ['POlic','POver','Polzovatel']
    list_filter = ('POlic',)


@admin.register(User1C)
class AdminUser1C(admin.ModelAdmin):
    list_display= ['User1C', 'Pas1C', 'DostupInt1C', 'PasInt1C', 'Otdel' ]
    search_fields = ('User1C__name','Otdel__Otdel')
    list_filter=('Otdel',)

@admin.register(VNCuser)
class AdminVNCUser(admin.ModelAdmin):
    list_display= ['UserVNC', 'IpVNC','HostVNC', 'PasVNC']
    search_fields= ('UserVNC__name', 'IpVNC', 'PasVNC', 'HostVNC')

@admin.register(OxranaCam)
class AdminOxranaCam(admin.ModelAdmin):
    list_display=['CamName','PodCam','CamIp','CamModel', 'LogPasCam','RTSPCam']
    search_fields=('CamName', 'CamIp')
