from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(max_length=100)
    