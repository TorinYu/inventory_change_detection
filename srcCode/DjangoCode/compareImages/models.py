from django.db import models

# Create your models here.
class photo(models.Model):
    image1 = models.ImageField(upload_to="image")
    image2 = models.ImageField(upload_to="image")
    time = models.DateTimeField('createTime', auto_now=True)