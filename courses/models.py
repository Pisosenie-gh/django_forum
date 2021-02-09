from django.db import models

# Create your models here.

class Courses(models.Model):
    photo = models.ImageField("Фото", upload_to='courses', blank=True)
    name = models.CharField("Название курса" , max_length=4000, null=True)
    price = models.CharField("Цена", max_length=5000, blank=True)
    hour = models.CharField("Часы", max_length=5000, blank=True)

    description = models.TextField("Описание", max_length=100000, null=True)
    slug = models.CharField("Ссылка на платежку" ,max_length= 50000, blank=True, null = True)


    class Meta:

        verbose_name = 'Курс'
        verbose_name_plural = "Курсы"


    def __str__(self):
        return str(self.name)


class Zayavka(models.Model):

    name = models.CharField("Название курса", max_length=4000, blank=True)
    fio = models.CharField("ФИО", max_length=4000, blank=True)
    iin = models.CharField("ИИН", max_length=20, blank=True)
    number = models.CharField("Номер телефона", max_length=40, blank=True)
    language = models.CharField("Язык обучения" , max_length=40, blank=True)


    class Meta:

        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name
