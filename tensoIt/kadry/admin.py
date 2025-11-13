from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Polzovatel, Otdel, Dolznost, Kontakti

@admin.register(Polzovatel)
class AdminPolzovatel(admin.ModelAdmin):
    list_display = ['name']
    search_fields= ('name',)


@admin.register(Otdel)
class AdminOtdel(admin.ModelAdmin):
    list_display = ['Otdel', 'Kommentariy']
    search_fields= ('Otdel', 'Kommentariy')

@admin.register(Dolznost)
class AdminDolznost(admin.ModelAdmin):
    pass

@admin.register(Kontakti)
class AdminKontakti(admin.ModelAdmin):
    list_display =  ('NumTel','PolzovatelKontakti', 'Dolznost', 'Otdel', 'MailAdress','get_image')
    readonly_fields=('get_image',)
    list_display_links= ('PolzovatelKontakti',)
    search_fields = ('PolzovatelKontakti__name', 'NumTel', )
    list_filter = ('Otdel','Podrazdel')
    readonly_fields= ('get_image1',)

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.photo.url} width="15%"')
    get_image.short_description='ФОТО'
    def get_image1(self, obj):
        return mark_safe(f'<img src= {obj.photo.url} width="45%"')
    get_image1.short_description='ФОТО'
