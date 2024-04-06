from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from datetime import datetime,timedelta
from User.models import tbl_cart

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
    
def productgallery(request,pid):
    productdata=tbl_rentitem.objects.get(id=pid)
    if request.method=="POST" and request.FILES:
        tbl_productgallery.objects.create(
        caption = request.POST.get("txt_caption"),
        image = request.FILES.get("txt_img")),
        rentitem=productdata
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

def sellercomplaint(request):
    sdata=tbl_newseller.objects.get(id=request.session['sid'])
    comdata=tbl_complainttype.objects.all()
    compdata=tbl_sellercomplaint.objects.all()
    if request.method=="POST":
        com=tbl_complainttype.objects.get(id=request.POST.get("select_com"))
        tbl_sellercomplaint.objects.create(    
            complainttitle = request.POST.get("txt_name"),
            content = request.POST.get("txt_content"),
            complainttype=com,
            seller=sdata,

        )
        return render(request,"Seller/SellerComplaint.html",{'sdata':sdata,'comdata':comdata,'compdata':compdata}) 
    else:
        return render(request,"Seller/SellerComplaint.html",{'sdata':sdata,'comdata':comdata,'compdata':compdata})


def DeleteComplaint(request,did):
    tbl_sellercomplaint.objects.get(id=did).delete()
    return redirect("Seller:SellerComplaint")        


def sellerfeedback(request):
    feeddata=tbl_sellerfeedback.objects.all()
    if request.method=="POST":
        tbl_sellerfeedback.objects.create(    
            feedback = request.POST.get("txt_feedback"),

        )
        return render(request,"Seller/SellerFeedBack.html",{'feeddata':feeddata}) 
    else:
        return render(request,"Seller/SellerFeedBack.html",{'feeddata':feeddata})

def DeleteFeedback(request,did):
    tbl_sellerfeedback.objects.get(id=did).delete()
    return redirect("Seller:SellerFeedBack")

def logout(request):
    del request.session["sid"]
    return redirect("Guest:Login")


def monthly_booking_report(request):    # Get the current date
    current_date = datetime.now()
    slr=tbl_newseller.objects.get(id=request.session["sid"])
    total=0
    # Calculate the first day and the last day of the current month  
    first_day_of_month = current_date.replace(day=1)
    last_day_of_month = first_day_of_month.replace(month=first_day_of_month.month + 1, day=1) - timedelta(days=1)
    # Query the database for bookings within the current month 
    # monthly_bookings = Booking.objects.filter(booking_date__range=[first_day_of_month, last_day_of_month])
    # Calculate the count of bookings for each day in the month
    data1=tbl_cart.objects.filter(booking__date__gte=first_day_of_month,booking__date__lte=last_day_of_month,product__seller=slr)
    for i in data1:
        if i.product.offerstatus=="Yes":
            total=total+(int(i.qty)*int(i.product.offerrate))
        else:
            total=total+(int(i.qty)*int(i.product.rate))
    return render(request,"Seller/MonthlyReport.html",{'data1':data1,'total':total}) 
    