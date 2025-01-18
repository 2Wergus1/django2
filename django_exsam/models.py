from django.db import models

class name(models.Model):
    name = models.CharField(max_length=100)
    malumot = models.IntegerField(verbose_name="Malumot kiriting")
    yosh = models.DateField(verbose_name="Yoshingizni kiriting")


def __str__(self):
        return self.name

class MyModel(models.Model):
    malumot = models.IntegerField(verbose_name="Malumot kiriting")
    yosh = models.DateField(verbose_name="Yoshingizni kiriting")

