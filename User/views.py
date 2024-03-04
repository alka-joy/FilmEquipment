from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *
from ServiceProvider.models import *
from Admin.models import *
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
    sdata=tbl_serviceprovider.objects.get(id=vid)
    rdata=tbl_services.objects.filter(serviceprovider=sdata)
    return render(request,"User/ViewServices.html",{'rdata':rdata})  

def searchserviceprovider(request):
    pdata=tbl_district.objects.all()
    rdata=tbl_serviceprovider.objects.all()
    parray=[]
    ar=[1,2,3,4,5]
    for i in rdata:
        sdata=tbl_serviceprovider.objects.get(id=i.id)
        totaldatacount=tbl_userrating.objects.filter(serviceprovider=sdata).count()
        totaldata=tbl_userrating.objects.filter(serviceprovider=sdata)
        sumdata=0
        for j in  totaldata:
            sumdata=sumdata+int(j.rating_data)
        if totaldatacount>0:
            avg=sumdata//totaldatacount
        else:
            avg=0
        parray.append(avg)
    datas=zip(rdata,parray)
    return render(request,"User/SearchServiceProvider.html",{'pdata':pdata,'rata':datas,'ar':ar})  

def servicebooking(request,bid):
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    bdata=tbl_services.objects.get(id=bid)
    if request.method=="POST":
        tbl_servicebooking.objects.create(
            booked_date=request.POST.get("txt_todate"),
            services=bdata,
            user=userdata,
        )
        return render(request,"User/Booking.html",{'bdata':bdata,'userdata':userdata}) 
    else:
        return render(request,"User/Booking.html",{'bdata':bdata,'userdata':userdata}) 

def viewservicebooking(request):
    userdata=tbl_newuser.objects.get(id=request.session["uid"])
    rdata=tbl_servicebooking.objects.filter(user=userdata)
    return render(request,"User/ViewServiceBooking.html",{'rdata':rdata})  

def usercomplaint(request):
    uregdata=tbl_newuser.objects.get(id=request.session['uid'])
    comdata=tbl_complainttype.objects.all()
    compdata=tbl_usercomplaint.objects.all()
    if request.method=="POST":
        com=tbl_complainttype.objects.get(id=request.POST.get("select_com"))
        tbl_usercomplaint.objects.create(    
            complainttitle = request.POST.get("txt_name"),
            content = request.POST.get("txt_content"),
            complainttype=com,
            user=uregdata,

        )
        return render(request,"User/UserComplaint.html",{'uregdata':uregdata,'comdata':comdata,'compdata':compdata}) 
    else:
        return render(request,"User/UserComplaint.html",{'uregdata':uregdata,'comdata':comdata,'compdata':compdata})

def DeleteComplaint(request,did):
    tbl_usercomplaint.objects.get(id=did).delete()
    return redirect("User:UserComplaint")        

def userfeedback(request):
    feeddata=tbl_userfeedback.objects.all()
    if request.method=="POST":
        tbl_userfeedback.objects.create(    
            feedback = request.POST.get("txt_feedback"),

        )
        return render(request,"User/UserFeedBack.html",{'feeddata':feeddata}) 
    else:
        return render(request,"User/UserFeedBack.html",{'feeddata':feeddata})

def DeleteFeedback(request,did):
    tbl_userfeedback.objects.get(id=did).delete()
    return redirect("User:UserFeedBack")   

def starrating(request,mid):
    parray=[1,2,3,4,5]
    wdata=tbl_serviceprovider.objects.get(id=mid)
    counts=0
    counts=stardata=tbl_userrating.objects.filter(serviceprovider=wdata).count()
    if counts>0:
        res=0
        stardata=tbl_userrating.objects.filter(serviceprovider=wdata).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        return render(request,"User/ShopRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/ShopRating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    
    wdata=tbl_serviceprovider.objects.get(id=workid)
    tbl_userrating.objects.create(user_name=user_name,user_review=user_review,rating_data=rating_data,serviceprovider=wdata)
    stardata=tbl_userrating.objects.filter(serviceprovider=wdata).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})  

def ajaxserviceprovider(request):
    if request.GET.get('pid')!="":
        placedata=tbl_place.objects.get(id=request.GET.get('pid'))
        rdata=tbl_serviceprovider.objects.filter(place=placedata)
        parray=[]
        ar=[1,2,3,4,5]
        for i in rdata:
            sdata=tbl_serviceprovider.objects.get(id=i.id)
            totaldatacount=tbl_userrating.objects.filter(serviceprovider=sdata).count()
            totaldata=tbl_userrating.objects.filter(serviceprovider=sdata)
            sumdata=0
            for j in  totaldata:
                sumdata=sumdata+int(j.rating_data)
            if totaldatacount>0:
                avg=sumdata//totaldatacount
            else:
                avg=0
            parray.append(avg)
        datas=zip(rdata,parray)
        return render(request,"User/AjaxServiceprovider.html",{'rata':datas,'ar':ar})
    else:
        placedata=tbl_district.objects.get(id=request.GET.get('did'))
        rdata=tbl_serviceprovider.objects.filter(place__district=placedata)
        parray=[]
        ar=[1,2,3,4,5]
        for i in rdata:
            sdata=tbl_serviceprovider.objects.get(id=i.id)
            totaldatacount=tbl_userrating.objects.filter(serviceprovider=sdata).count()
            totaldata=tbl_userrating.objects.filter(serviceprovider=sdata)
            sumdata=0
            for j in  totaldata:
                sumdata=sumdata+int(j.rating_data)
            if totaldatacount>0:
                avg=sumdata//totaldatacount
            else:
                avg=0
            parray.append(avg)
        datas=zip(rdata,parray)
        return render(request,"User/AjaxServiceprovider.html",{'rata':datas,'ar':ar})


def ajaxseller(request):
    if request.GET.get('pid')!="":
        placedata=tbl_place.objects.get(id=request.GET.get('pid'))
        ddata=tbl_newseller.objects.filter(place=placedata)
        return render(request,"User/AjaxSeller.html",{'data':ddata})
    else:
        placedata=tbl_district.objects.get(id=request.GET.get('did'))
        ddata=tbl_newseller.objects.filter(place__district=placedata)
        return render(request,"User/AjaxSeller.html",{'data':ddata})

def bill(request):
    if 'uid' in request.session:
        usr=tbl_newuser.objects.get(id=request.session["uid"])
        total=0
        
        if 'bookings' in request.session:
            rand=random.randint(100000,999999)
            cdate=date.today()
            bookdata=tbl_booking.objects.get(id=request.session["bookings"])
            wcartdata=tbl_cart.objects.filter(booking=bookdata)
            for i in wcartdata:
                total=total+(int(i.qty)*int(i.product.rate))
            sellerid=wcartdata[0].product.shop.id
            sellerdata=tbl_newshop.objects.get(id=sellerid)
            return render(request,"User/bill.html",{'wdata':wcartdata,'rand':rand,'cdate':cdate,'sellerdata':sellerdata,'usr':usr,'total':total})
        
        else:
            return render(request,"User/bill.html")
    else:
        return redirect("Guest:login")

def logout(request):
    del request.session["uid"]
    return redirect("Guest:Login")