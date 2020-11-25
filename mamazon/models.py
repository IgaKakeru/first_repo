from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/') #Pillowが必要

    def __str__(self):
        return self.name
