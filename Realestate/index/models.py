from django.db import models

# class Destination:
#     id :int
#     name:str
#     desc:str
#     price:int
#     img:str

# Create your models here.




###database

#
# class Destinations(models.Model):
#     name = models.CharField(max_length=50)
#     desc=models.TextField(max_length=100)
#     price=models.IntegerField()
#     img=models.ImageField(upload_to='pics')

class Locations(models.Model):
        name = models.CharField(max_length=50)
        desc = models.TextField(max_length=100)
        price = models.IntegerField()
        img = models.ImageField(upload_to='pics')
