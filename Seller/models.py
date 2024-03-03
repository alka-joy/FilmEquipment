from django.db import models
from Admin.models import *
# Create your models here.
from Guest.models import *


class tbl_rentitem(models.Model):
    name=models.CharField(max_length=50) 
    code=models.CharField(max_length=50)
    image=models.FileField(upload_to='Userdocs/')
    description=models.TextField()
    rate=models.TextField()
    features=models.CharField(max_length=50)
    stock=models.IntegerField()
    category=models.ForeignKey(tbl_rentcategory,on_delete=models.CASCADE)
    seller=models.ForeignKey(tbl_newseller,on_delete=models.SET_NULL,null=True)
class tbl_productgallery(models.Model):
    caption=models.CharField(max_length=50)
    image=models.FileField(upload_to='Userdocs/')
    rentitem=models.ForeignKey(tbl_rentitem,on_delete=models.SET_NULL,null=True)

class tbl_sellercomplaint(models.Model):  
    complainttype=models.ForeignKey(tbl_complainttype,on_delete=models.CASCADE)
    complainttitle=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    complaintdate=models.DateField(auto_now_add=True) 
    seller=models.ForeignKey(tbl_newseller,on_delete=models.SET_NULL,null=True)        


class tbl_sellerfeedback(models.Model):  
    feedback=models.CharField(max_length=50)
    feedbackdate=models.DateField(auto_now_add=True) 
    