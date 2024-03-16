from django.db import models

# Create your models here.
class categorydb(models.Model):
    objects = None

    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Images", null=True, blank=True)

    Description = models.CharField(max_length=100,null=True, blank=True)

class productdb(models.Model):
     objects = None
     CategoryName = models.CharField(max_length=100, null=True, blank=True)
     ProductName = models.CharField(max_length=100, null=True, blank=True)
     Price = models.IntegerField(null=True, blank=True)
     Description = models.CharField(max_length=100, null=True, blank=True)
     ProductImage = models.ImageField(upload_to="Images", null=True, blank=True)
