from django.db import models


class Main(models.Model):
    name = models.CharField('Название', max_length=255)

    description = models.CharField('Описание', max_length=255)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name
