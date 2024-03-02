from django.db import models
from  Admin.models import *
from Guest.models import *
# Create your models here.

class tbl_services(models.Model):
    name=models.CharField(max_length=50)
    rate=models.IntegerField()
    details=models.CharField(max_length=50)
    service=models.ForeignKey(tbl_service,on_delete=models.CASCADE)
    serviceprovider=models.ForeignKey(tbl_serviceprovider,on_delete=models.CASCADE)