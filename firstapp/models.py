from django.db import models

class bookdata(models.Model):
    num = models.IntegerField(default=1)
    name = models.CharField(max_length=200)
    names = models.CharField(max_length=200,default='Нету')
    avtor = models.CharField(max_length=200)
    janr = models.CharField(max_length=200)
    star = models.IntegerField()
    place = models.CharField(max_length=200)
    aboutbook = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='',default='SOME STRING')
class logindata(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)