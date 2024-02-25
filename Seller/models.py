from django.db import models
from Admin.models import *
# Create your models here.
from Guest.models import *
class tbl_productgallery(models.Model):
    caption=models.CharField(max_length=50)
    image=models.FileField(upload_to='Userdocs/')

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