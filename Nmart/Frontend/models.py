from django.db import models

# Create your models here.
class contactdb(models.Model):

    objects = None
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)
class logindb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)

class cartdb(models.Model):
    objects = None
    Username=models.CharField(max_length=100,null=True,blank=True)


    Size=models.CharField(max_length=100,null=True,blank=True)
    Productname=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)
class checkoutdb(models.Model):
    FirstName=models.CharField(max_length=100,null=True,blank=True)
    LastName=models.CharField(max_length=100,null=True,blank=True)

    Country=models.CharField(max_length=100,null=True,blank=True)
    Street=models.CharField(max_length=100,null=True,blank=True)

    Postcode=models.IntegerField(null=True,blank=True)
    Town=models.CharField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)

