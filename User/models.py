from django.db import models
from Guest.models import *
from Seller.models import *
from ServiceProvider.models import *
# Create your models here.

class tbl_booking(models.Model):
    status=models.IntegerField(default=0) 
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)

class tbl_cart(models.Model):
    qty=models.IntegerField(default=1)
    cstatus=models.IntegerField(default=0) 
    product=models.ForeignKey(tbl_rentitem,on_delete=models.CASCADE)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)

class tbl_servicebooking(models.Model):
    services=models.ForeignKey(tbl_services,on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    booked_date=models.DateField()
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)


class tbl_usercomplaint(models.Model):  
    complainttype=models.ForeignKey(tbl_complainttype,on_delete=models.CASCADE)
    complainttitle=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    complaintdate=models.DateField(auto_now_add=True) 
    user=models.ForeignKey(tbl_newuser,on_delete=models.SET_NULL,null=True)    