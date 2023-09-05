from django.db import models
from django.db import models

# Create your models here.

class main(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    path = models.ImageField(upload_to='images/site')


class CardProduct(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')

class ConteudoSegundoMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')