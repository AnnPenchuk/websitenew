from django.db import models


class Main(models.Model):
    name = models.CharField('ФИО', max_length=255)

    experience = models.CharField('Опыт работы', max_length=255)

    phone = models.CharField('Номер телефона', max_length=255)

    address = models.CharField('Адрес', max_length=255)


    def __str__(self):
        return self.name
