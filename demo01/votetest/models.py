from django.db import models

# Create your models here.


class Question(models.Model):
    qname = models.CharField(max_length=50)
    qpoll = models.IntegerField(default=0)

    def __str__(self):
        return self.qname

    def name(self):
        return self.qname
    name.short_description = '问题'

    def poll(self):
        return self.qpoll
    poll.short_description = '参与人次'


class Choice(models.Model):
    cname = models.CharField(max_length=20)
    cpoll = models.IntegerField(default=0)
    cque = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

    def name(self):
        return self.cname
    name.short_description = '问题选项'

    def poll(self):
        return self.cpoll
    poll.short_description = '票数'

    def que(self):
        return self.cque
    que.short_description = '问题'

