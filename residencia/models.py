from django.contrib.auth.models import User
from django.db import models


class Residencia(models.Model):
    morador = models.ManyToManyField(User)
    numero = models.IntegerField()

    def __int__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Residências"


class Bloco(models.Model):
    identificacao = models.CharField(max_length=40)
    residencias = models.ManyToManyField(Residencia)

    def __str__(self):
        return self.identificacao

    class Meta:
        verbose_name_plural = "Blocos"
