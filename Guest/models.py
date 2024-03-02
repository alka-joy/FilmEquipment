from django.db import models
from Admin.models import *
# Create your models here.


class tbl_newuser(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=50)
    address=models.TextField()
    password=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_newseller(models.Model):
    name=models.CharField(max_length=50) 
    contact=models.IntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=50) 
    address=models.TextField()
    photo=models.FileField(upload_to='Userdocs/')  
    proof=models.FileField(upload_to='Userdocs/')
    password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,default=0,null=True)
    
class tbl_serviceprovider(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=50)
    address=models.TextField()
    password=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_adminlogin(models.Model):
    name=models.CharField(max_length=15)
    email=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
