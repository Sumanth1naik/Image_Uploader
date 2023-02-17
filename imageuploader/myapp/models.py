from django.db import models

# Create your models here.
class Image(models.Model):
    Photo=models.ImageField(upload_to="my_images")  #here we can declare the path where image should be stored
    date = models.DateTimeField(auto_now_add=True)
