import datetime
from django.db import models
from django.utils import timezone

class Job(models.Model):
    job_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
   # def __str__(self) :
    #    return "{}".format(self.job_text)


class Choice(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
  # def __str__(self):
   #     return self.choice_text
    #def was_published_recently(self):
     #   return self.pub_date >= timezone.now() - datetime.timedelta(day = 1)
