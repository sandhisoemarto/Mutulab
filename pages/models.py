from django.db import models


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Update')
    bodytext = models.TextField('Page Content', blank=True)
