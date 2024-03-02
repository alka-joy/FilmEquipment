from django.shortcuts import render,redirect
from Guest.models import *
from ServiceProvider.models import *
from Admin.models import *
from User.models import *

# Create your views here.

def serviceproviderhome(request):
    udata=tbl_serviceprovider.objects.get(id=request.session['spid'])
    return render(request,"ServiceProvider/ServiceProviderHome.html",{'udata':udata})

def myprofile(request):
    udata=tbl_serviceprovider.objects.get(id=request.session['spid'])
    return render(request,"ServiceProvider/MyProfile.html",{'udata':udata})    

def editprofile(request):
    udata=tbl_serviceprovider.objects.get(id=request.session['spid'])
    if request.method=="POST":
        udata.name=request.POST.get("txt_name")
        udata.contact=request.POST.get("txt_con")
        udata.email=request.POST.get("txt_email")
        udata.address=request.POST.get("txt_address")
        udata.save()
        return redirect("ServiceProvider:MyProfile")
    else:
        return render(request,"ServiceProvider/EditProfile.html",{'udata':udata})

def changepassword(request):
    udata=tbl_serviceprovider.objects.get(id=request.session['spid'])
    if request.method=="POST":
        pwd=udata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                udata.password=pass1
                udata.save()
                return redirect("ServiceProvider:ChangePassword")
            else:
                msg= "Password donot match"
                return render(request,"ServiceProvider/ChangePassword.html",{'msg':msg})
        else:
            msg="Incorrect password"
            return render(request,"ServiceProvider/ChangePassword.html",{'msg':msg})
    else:
        msg="Password changed"
        return render(request,"ServiceProvider/ChangePassword.html")
    
def services(request):
    serviceproviderdata=tbl_serviceprovider.objects.get(id=request.session["spid"])
    disdata=tbl_service.objects.all()
    data=tbl_services.objects.filter(serviceprovider=serviceproviderdata)
    if request.method=="POST":
        dis=tbl_service.objects.get(id=request.POST.get("select_ser"))
        tbl_services.objects.create(
        name = request.POST.get("txt_name"),
        rate = request.POST.get("txt_rate"),
        details = request.POST.get("txt_detail"),
        service=dis,
        serviceprovider=serviceproviderdata)
        return render(request,"ServiceProvider/Services.html",{'disdata':disdata,'data':data})
    else:
        return render(request,"ServiceProvider/Services.html",{'disdata':disdata,'data':data})


def DeleteServices(request,did):
    tbl_services.objects.get(id=did).delete()
    return redirect("ServiceProvider/Services")        


def EditServices(request,eid):
    dis=tbl_services.objects.get(id=eid)
    if request.method=="POST":
        dis.service_name=request.POST.get("txt_service")
        dis.save()
        return redirect("ServiceProvider/Services")  
    else:
        return render(request,"ServiceProvider/Services",{'edis':dis})  

def viewbooking(request):
    rdata=tbl_servicebooking.objects.all()
    return render(request,"ServiceProvider/ViewBooking.html",{'rdata':rdata})  
