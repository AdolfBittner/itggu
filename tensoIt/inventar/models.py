from django.db import models
from kadry.models import Polzovatel, Otdel

class Computer(models.Model):
    inventarNum = models.CharField('Инвентарный номер', max_length=10, unique=True)
    Podrazdelenie = models.CharField('Подразделение',max_length=30)
    SetevoeImya = models.CharField('Сетевое имя',max_length=30)
    TipPK = models.CharField('Тип ПК',max_length=30)
    Konfiguracia = models.CharField('Конфигурация ПК',max_length=80)
    OS = models.CharField('ОС', max_length=30)
    Office = models.CharField('Офис', max_length=30)
    VPNUser = models.CharField('VPN пользователь', max_length=30)
    VPNIp = models.CharField('VPN Ip', max_length=30)
    VPNPas= models.CharField('VPN пароль', max_length=20)
    DataPokupki = models.CharField('Дата покупки',max_length=30)
    Polzovatel = models.ForeignKey(Polzovatel, verbose_name='Пользователь', on_delete=models.CASCADE)
    Kommentariy = models.TextField('Комментарий', blank=True)



    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'
    def __str__(self):
        return self.Konfiguracia


class Printer (models.Model):
    PrintModel=models.CharField('Модель', max_length=30)
    TipPrint=models.CharField('Тип принтера', max_length=65)
    Mesto=models.CharField('Местонахождение', max_length=65)
    SetPrint=models.CharField('IP адрес', max_length=70)
    Kommentariy=models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return self.PrintModel

class TensoMail(models.Model):
    MailAdr= models.CharField('Адрес почты', max_length=40, unique=True)
    MailPass=models.CharField('Пароль', max_length=30)
    UserMail= models.ForeignKey(Polzovatel, verbose_name='Пользователь', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Почту'
        verbose_name_plural = 'Почта'

    def __str__(self):
        return self.MailAdr


class License(models.Model):
    POlic=models.CharField('ПО', max_length=40)
    POver=models.CharField('Версия', max_length=50)
    POkey=models.CharField('Лицензия', max_length=50)

    Polzovatel= models.ForeignKey(Polzovatel, verbose_name='Пользователи', on_delete =models.CASCADE)
    class Meta:
        verbose_name = 'Лицензию'
        verbose_name_plural = 'Лицензии'

        def __str__(self):
            return self.POlic

class User1C(models.Model):
    User1C=models.ForeignKey(Polzovatel, verbose_name='Пользователь', on_delete = models.CASCADE)
    Pas1C=models.CharField('Пароль', max_length=20)
    DostupInt1C=models.CharField('Доступ из интернета', max_length=20, blank=True )
    PasInt1C=models.CharField('Пароль для интернет 1С', max_length=20, blank=True)
    Otdel=models.ForeignKey(Otdel, verbose_name='Отдел', on_delete=models.CASCADE)
    class Meta:
        verbose_name= 'Пользователя 1С'
        verbose_name_plural='Пользователи 1С'

        def __str__(self):
            return self.User

class VNCuser(models.Model):
    UserVNC=models.ForeignKey(Polzovatel, verbose_name='Пользователь', on_delete= models.CASCADE)
    IpVNC=models.CharField('IP адрес', max_length=30)
    HostVNC=models.CharField('HostName', max_length=40)
    PasVNC=models.CharField('Пароль VNC', max_length=30)
    class Meta:
        verbose_name='VNC'
        verbose_name_plural='VNC'

        def __str__(self):
            return self.UserVNC

class OxranaCam(models.Model):
    CamName = models.CharField('Имя', max_length=30 )
    PodCam=models.CharField('Отдел', max_length=10)
    CamIp = models.CharField('IP', max_length=20)
    CamModel = models.CharField('Модель', max_length=30)
    LogPasCam=models.CharField('Логин/Пароль', max_length=15)
    RTSPCam = models.CharField('RTSP ссылка', max_length=60)
    CamKoment = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name='Камеру'
        verbose_name_plural='Камеры'
        def __str__(self):
            return self.CamName
