from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
# Create your views here.

def sellerhome(request):
    sdata=tbl_newseller.objects.get(id=request.session['sid'])
    return render(request,"Seller/SellerHome.html",{'sdata':sdata})


def myprofile(request):
    sdata=tbl_newseller.objects.get(id=request.session['sid'])
    return render(request,"Seller/MyProfile.html",{'sdata':sdata})    

def editprofile(request):
    sdata=tbl_newseller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        sdata.name=request.POST.get("txt_name")
        sdata.contact=request.POST.get("txt_con")
        sdata.email=request.POST.get("txt_email")
        sdata.address=request.POST.get("txt_address")
        sdata.save()
        return redirect("Seller:MyProfile")
    else:
        return render(request,"Seller/EditProfile.html",{'sdata':sdata})

def changepassword(request):
    sdata=tbl_newseller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        pwd=sdata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                sdata.password=pass1
                sdata.save()
                return redirect("Seller:ChangePassword")
            else:
                msg= "Password donot match"
                return render(request,"Seller/ChangePassword.html",{'msg':msg})
        else:
            msg="Incorrect password"
            return render(request,"Seller/ChangePassword.html",{'msg':msg})
    else:
        msg="Password changed"
        return render(request,"Seller/ChangePassword.html")
    
def productgallery(request):
    if request.method=="POST" and request.FILES:
        tbl_productgallery.objects.create(
        caption = request.POST.get("txt_caption"),
        image = request.FILES.get("txt_img"))
        return render(request,"Seller/ProductGallery.html")
    else:
        return render(request,"Seller/ProductGallery.html")

def rentitem(request):
    sdata=tbl_newseller.objects.get(id=request.session['sid'])
    rdata=tbl_rentitem.objects.filter(seller=sdata)
    categoryid=tbl_rentcategory.objects.all()
    if request.method=="POST" and request.FILES:
        categorydata=tbl_rentcategory.objects.get(id=request.POST.get('select_category'))
        tbl_rentitem.objects.create(
        name = request.POST.get("txt_name"),
        code = request.POST.get("txt_code"),
        image = request.FILES.get("txt_img"),
        description = request.POST.get("txt_dis"),
        rate = request.POST.get("txt_rate"),
        category = categorydata,
        features = request.POST.get("txt_features"),
        stock = request.POST.get("txt_stock"),
        seller=sdata)
        return render(request,"Seller/RentItem.html",{'rdata':rdata,'categoryid':categoryid})
    else:
        return render(request,"Seller/RentItem.html",{'rdata':rdata,'categoryid':categoryid})

def DeleteRentItem(request,did):
    tbl_rentitem.objects.get(id=did).delete()
    return redirect("Seller:RentItem")     

def searchseller(request):
    pdata=tbl_district.objects.all()
    ddata=tbl_place.objects.all()
    if request.method=="POST":  
        return render(request,"Seller/SearchSeller.html",{'pdata':pdata})  
    else:
        return render(request,"Seller/SearchSeller.html",{'pdata':pdata})

def ajaxplace(request):
    disob=tbl_district.objects.get(id=request.GET.get('Dist'))
    places=tbl_place.objects.filter(district=disob)
    return render(request,"Seller/AjaxPlace.html",{'plc':places})
