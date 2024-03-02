from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
# Create your views here.


def user(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get("select_dis"))
        tbl_newuser.objects.create(
        name = request.POST.get("txt_name"),
        contact = request.POST.get("txt_con"),
        email = request.POST.get("txt_email"),
        address = request.POST.get("txt_add"),
        password = request.POST.get("txt_pass"),
        district=dis)
        return render(request,"Guest/NewUser.html",{'disdata':disdata})
    else:
        return render(request,"Guest/NewUser.html",{'disdata':disdata})


def seller(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST" and request.FILES:
        placeid=tbl_place.objects.get(id=request.POST.get("select_place"))
        tbl_newseller.objects.create(
        name = request.POST.get("txt_name"),
        contact = request.POST.get("txt_con"),
        email = request.POST.get("txt_email"),
        gender = request.POST.get("btn_gen"),
        address = request.POST.get("txt_add"),
        place = placeid,
        photo = request.FILES.get("txt_pic"),
        proof = request.FILES.get("txt_proof"),
        password = request.POST.get("txt_pass"))
        return render(request,"Guest/NewSeller.html",{'disdata':disdata})
    else:
        return render(request,"Guest/NewSeller.html",{'disdata':disdata})

def ajaxplace(request):
    disob=tbl_district.objects.get(id=request.GET.get('Dist'))
    places=tbl_place.objects.filter(district=disob)
    return render(request,"Guest/AjaxPlace.html",{'plc':places})


def login(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_pass')

        ucount=tbl_newuser.objects.filter(email=Email,password=Password).count()
        scount=tbl_newseller.objects.filter(email=Email,password=Password,status=1).count()
        spcount=tbl_serviceprovider.objects.filter(email=Email,password=Password).count()
        acount=tbl_adminlogin.objects.filter(email=Email,password=Password).count()
        if ucount > 0:
            userdata=tbl_newuser.objects.get(email=Email,password=Password)
            request.session['uid']=userdata.id
            return redirect('User:UserHome')
        elif scount > 0:
            sellerdata=tbl_newseller.objects.get(email=Email,password=Password)
            request.session['sid']=sellerdata.id
            return redirect('Seller:SellerHome')
        elif spcount>0:
            servicedata=tbl_serviceprovider.objects.get(email=Email,password=Password)
            request.session['spid']=servicedata.id
            return redirect('ServiceProvider:ServiceProviderHome')
        elif acount>0:
            addata=tbl_adminlogin.objects.get(email=Email,password=Password)
            request.session['aid']=addata.id
            return redirect('Admin:AdminHome')  
        else:
            msg = "Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")

def index(request):
    return render(request,"Guest/index.html")

def serviceprovider(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get("select_dis"))
        tbl_serviceprovider.objects.create(
        name = request.POST.get("txt_name"),
        contact = request.POST.get("txt_con"),
        email = request.POST.get("txt_email"),
        address = request.POST.get("txt_add"),
        password = request.POST.get("txt_pass"),
        district=dis)
        return render(request,"Guest/ServiceProvider.html",{'disdata':disdata})
    else:
        return render(request,"Guest/ServiceProvider.html",{'disdata':disdata})
