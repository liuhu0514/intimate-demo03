from django.db import models

# Create your models here.


class Question(models.Model):
    qname = models.CharField(max_length=50)
    qpoll = models.IntegerField(default=0)


class Choice(models.Model):
    cname = models.CharField(max_length=20)
    cpoll = models.IntegerField(default=0)
    cque = models.ForeignKey('Question', on_delete=models.CASCADE)

