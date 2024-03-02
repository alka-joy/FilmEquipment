from django.shortcuts import render,redirect
from .models import *
from Guest.models import *
from Seller.models import *
from User.models import *
# Create your views here.

def dis(request):
    disdata=tbl_district.objects.all()
    if request.method=="POST":
        datacount=tbl_district.objects.filter(district_name=request.POST.get("txt_district")).count()
        if datacount>0:
            return render(request,"Admin/District.html",{'district':disdata})
        else:

            tbl_district.objects.create(district_name=request.POST.get("txt_district"))
            return render(request,"Admin/District.html",{'district':disdata})
    else:
        return render(request,"Admin/District.html",{'district':disdata})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")        


def EditDistrict(request,eid):
    dis=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        dis.district_name=request.POST.get("txt_district")
        dis.save()
        return redirect("Admin:District")  
    else:
        return render(request,"Admin/District.html",{'edis':dis})  


def pl(request):
    disdata=tbl_district.objects.all()
    subdata=tbl_place.objects.all()
    if request.method=="POST":
        dis = tbl_district.objects.get(id=request.POST.get("select_dis"))
        datacount=tbl_place.objects.filter(place_name=request.POST.get("txt_place"),
            district=dis).count()
        if datacount>0:
            return render(request,"Admin/Place.html",{'disdata':disdata,'subcat':subdata})
        else:
            tbl_place.objects.create(
            place_name=request.POST.get("txt_place"),
            district=dis
            )
            return render(request,"Admin/Place.html",{'disdata':disdata,'subcat':subdata})
    else:    
        return render(request,"Admin/Place.html",{'disdata':disdata,'subcat':subdata})

def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")          

def ser(request):
    disdata=tbl_service.objects.all()
    if request.method=="POST":
        datacount=tbl_service.objects.filter(service_name=request.POST.get("txt_service"))
        if datacount>0:
            return render(request,"Admin/Service.html",{'service':disdata})
        else:    
            tbl_service.objects.create(service_name=request.POST.get("txt_service"))
            return render(request,"Admin/Service.html",{'service':disdata})
    else:
        return render(request,"Admin/Service.html",{'service':disdata})

def DeleteService(request,did):
    tbl_service.objects.get(id=did).delete()
    return redirect("Admin:Service")        


def EditService(request,eid):
    dis=tbl_service.objects.get(id=eid)
    if request.method=="POST":
        dis.service_name=request.POST.get("txt_service")
        dis.save()
        return redirect("Admin:Service")  
    else:
        return render(request,"Admin/Service.html",{'edis':dis})  


def com(request):
    disdata=tbl_complainttype.objects.all()
    if request.method=="POST":
        datacount=tbl_complainttype.objects.filter(complaint_name=request.POST.get("txt_complaint")).count()
        if datacount>0:
            return render(request,"Admin/ComplaintType.html",{'complaint':disdata})
        else:
            tbl_complainttype.objects.create(complaint_name=request.POST.get("txt_complaint"))
            return render(request,"Admin/ComplaintType.html",{'complaint':disdata})
    else:
        return render(request,"Admin/ComplaintType.html",{'complaint':disdata})

def DeleteComplaint(request,did):
    tbl_complainttype.objects.get(id=did).delete()
    return redirect("Admin:Complaint")        


def EditComplaint(request,eid):
    dis=tbl_complainttype.objects.get(id=eid)
    if request.method=="POST":
        dis.complaint_name=request.POST.get("txt_complaint")
        dis.save()
        return redirect("Admin:Complaint")  
    else:
        return render(request,"Admin/ComplaintType.html",{'edis':dis})  

def cat(request):
    disdata=tbl_rentcategory.objects.all()
    if request.method=="POST":
        tbl_rentcategory.objects.create(category_name=request.POST.get("txt_category"))
        return render(request,"Admin/RentCategory.html",{'category':disdata})
    else:
        return render(request,"Admin/RentCategory.html",{'category':disdata})

def DeleteCategory(request,did):
    tbl_rentcategory.objects.get(id=did).delete()
    return redirect("Admin:Category")        


def EditCategory(request,eid):
    dis=tbl_rentcategory.objects.get(id=eid)
    if request.method=="POST":
        dis.category_name=request.POST.get("txt_category")
        dis.save()
        return redirect("Admin:Category")  
    else:
        return render(request,"Admin/RentCategory.html",{'edis':dis})  

def shop(request):
    disdata=tbl_newseller.objects.all()
    return render(request,"Admin/NewShop.html",{'data':disdata})


def sellerlist(request):
    selldata=tbl_newseller.objects.filter(status=0)
    return render(request,"Admin/ViewNewSeller.html",{'selldata':selldata})

def acceptedsellerlist(request):
    selldata=tbl_newseller.objects.filter(status=1)
    return render(request,"Admin/AcceptedSellerList.html",{'selldata':selldata})

def rejectedsellerlist(request):
    selldata=tbl_newseller.objects.filter(status=2)
    return render(request,"Admin/RejectedSellerList.html",{'selldata':selldata})

def acceptseller(request,aid):
    sellerdata=tbl_newseller.objects.get(id=aid)
    sellerdata.status=1
    sellerdata.save()
    return redirect("Admin:ViewNewSeller")

def rejectseller(request,rid):
    sellerdata=tbl_newseller.objects.get(id=rid)
    sellerdata.status=2
    sellerdata.save()
    return redirect("Admin:ViewNewSeller")

def adminhome(request):
    return render(request,"Admin/AdminHome.html")


def viewsellercomplaint(request):
    rdata=tbl_sellercomplaint.objects.all()
    return render(request,"Admin/ViewSellerComplaint.html",{'rdata':rdata})  


def viewusercomplaint(request):
    udata=tbl_usercomplaint.objects.all()
    return render(request,"Admin/ViewUserComplaint.html",{'udata':udata})  

def viewuserfeedback(request):
    udata=tbl_userfeedback.objects.all()
    return render(request,"Admin/ViewUserFeedback.html",{'udata':udata})  

def viewsellerfeedback(request):
    udata=tbl_sellerfeedback.objects.all()
    return render(request,"Admin/ViewSellerFeedback.html",{'udata':udata})  
