from django.db import models


class Polzovatel(models.Model):
    name = models.CharField('Сотрудник ФИО', max_length=70, unique=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name

class Otdel(models.Model):
    Otdel=models.CharField('Отдел', max_length=80)
    Kommentariy=models.TextField('Комментарий', max_length=80)
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
    def __str__(self):
        return self.Otdel

class Dolznost(models.Model):
    Dolznost=models.CharField('Должность', max_length=50)
    Kommentariy=models.CharField('Комментарий', max_length=70, blank=True)
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
    def __str__(self):
        return self.Dolznost


class Kontakti(models.Model):
    NumTel = models.CharField('Телефон',max_length=30)
    PolzovatelKontakti = models.ForeignKey(Polzovatel, verbose_name='Пользователь', on_delete=models.CASCADE)
    Dolznost = models.ForeignKey(Dolznost, verbose_name='Должность', on_delete=models.CASCADE)
    Otdel= models.ForeignKey(Otdel, verbose_name = 'Отдел', on_delete=models.CASCADE)
    Podrazdel=models.CharField('Подразделение', max_length=80, blank=True)
    MailAdress=models.ForeignKey('inventar.TensoMail',verbose_name = 'Почта', on_delete = models.CASCADE)
    photo=models.ImageField('фотография', upload_to='kadry/photos', default='kadry/photos/default.jpg')
    kabinet=models.CharField('Кабинет', max_length=15, blank=True )
    mob=models.CharField('Мобильный телефон', max_length=30, blank =True)


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
    def __str__(self):
        return self.NumTel
