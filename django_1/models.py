# from django.db import models
#
# class name(models.Model):
#     name = models.CharField(max_length=100)
#     malumot = models.IntegerField(verbose_name="Malumot kiriting")
#     yosh = models.DateField(verbose_name="Yoshingizni kiriting")
#
#
# def __str__(self):
#         return self.name
#
# class MyModel(models.Model):
#     malumot = models.IntegerField(verbose_name="Malumot kiriting")
#     yosh = models.DateField(verbose_name="Yoshingizni kiriting")
from django.conf import settings
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

class UserModel(AbstractUser):
    pass


