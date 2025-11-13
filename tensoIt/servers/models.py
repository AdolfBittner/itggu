from django.db import models

class Server(models.Model):
    name = models.CharField('Название или IP', max_length=70, unique=True)
    ipadr = models.CharField('IP адресс', max_length=70, unique=True)
    description = models.CharField('Описание', max_length=300)
    hardware = models.CharField('Характеристики', max_length=300 )
    inwork = models.BooleanField('В работе')
    comment = models.TextField('Комментарий', blank = True)
    yearstart = models.CharField('Год запуска', max_length = 30, blank = True)


    class Meta:
        verbose_name = 'Сервер'
        verbose_name_plural = 'Сервера'

    def __str__(self):
        return self.name

class VirtualServer(models.Model):
    name = models.CharField('Название', max_length=80, unique=True)
    hardServer = models.ForeignKey(Server, verbose_name='Физический сервер', on_delete=models.CASCADE)
    description = models.CharField('Описание', max_length=300)
    osVirt = models.CharField('Операционная система', max_length=70)
    virthardware = models.CharField('Выделенно ресурсов', max_length = 300)
    ipadr = models.CharField('IP адресс', max_length=70, unique=True)
    inwork = models.BooleanField('В работе')
    comment = models.TextField('Комментарий', blank = True)

    class Meta:
        verbose_name = 'Виртуальный сервер'
        verbose_name_plural = 'Виртуальные сервера'

    def __str__(self):
        return self.name
