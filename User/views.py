from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *
from ServiceProvider.models import *
# Create your views here.

def userhome(request):
    udata=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,"User/UserHome.html",{'udata':udata})

def myprofile(request):
    udata=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'udata':udata})    

def editprofile(request):
    udata=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        udata.name=request.POST.get("txt_name")
        udata.contact=request.POST.get("txt_con")
        udata.email=request.POST.get("txt_email")
        udata.address=request.POST.get("txt_address")
        udata.save()
        return redirect("User:MyProfile")
    else:
        return render(request,"User/EditProfile.html",{'udata':udata})


def changepassword(request):
    udata=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        pwd=udata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                udata.password=pass1
                udata.save()
                return redirect("User:ChangePassword")
            else:
                msg= "Password donot match"
                return render(request,"User/ChangePassword.html",{'msg':msg})
        else:
            msg="Incorrect password"
            return render(request,"User/ChangePassword.html",{'msg':msg})
    else:
        msg="Password changed"
        return render(request,"User/ChangePassword.html")
    
def viewproducts(request,sid):
    categoryid=tbl_rentcategory.objects.all()
    request.session["seller"]=sid
    sdata=tbl_newseller.objects.get(id=sid)
    rdata=tbl_rentitem.objects.filter(seller=sdata)
    return render(request,"User/ViewProducts.html",{'rdata':rdata,'categoryid':categoryid,'sdata':sdata})

def ajaxcategory(request):
    sdata=tbl_newseller.objects.get(id=request.session["seller"])
    adata=tbl_rentcategory.objects.get(id=request.GET.get('Dist'))
    rdata=tbl_rentitem.objects.filter(category=adata,seller=sdata)
    return render(request,"User/AjaxCategory.html",{'rdata':rdata})


def searchseller(request):
    pdata=tbl_district.objects.all()
    ddata=tbl_newseller.objects.all()
    return render(request,"User/SearchSeller.html",{'pdata':pdata,'data':ddata})  
    

def addtocart(request,rid):
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    rentdata=tbl_rentitem.objects.get(id=rid)
    bcount=tbl_booking.objects.filter(user=userdata,status=0).count()
    if bcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,status=0)
        ccount=tbl_cart.objects.filter(booking=bookingdata,product=rentdata).count()
        if ccount>0:
            print("Already in Cart")
            return redirect("User:SearchSeller")
        else:
            tbl_cart.objects.create(product=rentdata,booking=bookingdata)
            return redirect("User:SearchSeller")
    else:
        tbl_booking.objects.create(user=userdata)
        bcount=tbl_booking.objects.filter(user=userdata,status=0).count()
        if bcount>0: 
            bookingdata=tbl_booking.objects.get(user=userdata,status=0)
            ccount=tbl_cart.objects.filter(booking=bookingdata,product=rentdata).count()
            if ccount>0:
                print("Already in Cart")
                return redirect("User:SearchSeller")
            else:
                tbl_cart.objects.create(product=rentdata,booking=bookingdata)
                return redirect("User:SearchSeller")

def mycart(request):
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    cdata=tbl_cart.objects.filter(booking__user=userdata)
    if request.method=="POST":
        for i in cdata:
            productdata=tbl_rentitem.objects.get(id=i.product.id)
            stock=int(productdata.stock)
            newstock=stock-int(i.qty)
            productdata.stock=newstock
            productdata.save()
        request.session["total"]=request.POST.get('carttotalamt')
        return redirect("User:Payment")
    else:
        return render(request,"User/MyCart.html",{'userdata':userdata,'cdata':cdata})

def get_qnty(request):
        qty=request.GET.get('QTY')
        alt=request.GET.get('ALT')
        cart=tbl_cart.objects.get(id=alt)
        cart.qty=qty
        cart.save()
        return redirect('User:MyCart')


def removecart(request,did):
    tbl_cart.objects.get(id=did).delete()
    return redirect('User:MyCart')

def payment(request):
    data=request.session["total"]
    return render(request,"User/Payment.html",{'amount':data})

def viewservices(request,vid):
    rdata=tbl_services.objects.all()
    return render(request,"User/ViewServices.html",{'rdata':rdata})  

def searchserviceprovider(request):
    pdata=tbl_district.objects.all()
    rdata=tbl_serviceprovider.objects.all()
    return render(request,"User/SearchServiceProvider.html",{'pdata':pdata,'rata':rdata})  

def servicebooking(request,bid):
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    bdata=tbl_services.objects.get(id=bid)
    if request.method=="POST":
        tbl_servicebooking.objects.create(
            booked_date=request.POST.get("txt_todate"),
            services=bdata,
            user=userdata,
        )
        return render(request,"User/ServiceBooking.html",{'bdata':bdata,'userdata':userdata}) 
    else:
        return render(request,"User/ServiceBooking.html",{'bdata':bdata,'userdata':userdata}) 

def viewservicebooking(request):
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    rdata=tbl_servicebooking.objects.filter(user=userdata)
    return render(request,"User/ViewServiceBooking.html",{'rdata':rdata})  
