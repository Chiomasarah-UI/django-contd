from django.db import models

class post(models.Model):
    title = models.CharField(max_length=200)
    text =  models.TextField(max_length=200)
    author = models.ForeignKey
    Created_date = models.DateTimeField(max_length=200)
    Publish_date = models.DateTimeField(max_length=180)
