from django.urls import path
from User import views

app_name='User'

urlpatterns = [
    path('userhome/',views.userhome,name="UserHome"),
    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofile/',views.editprofile,name="EditProfile"),
    path('changepassword/',views.changepassword,name="ChangePassword"),
    path('viewproducts/<int:sid>',views.viewproducts,name="ViewProducts"),
    path('AjaxCategory/',views.ajaxcategory,name="AjaxCategory"),
    path('searchseller/',views.searchseller,name="SearchSeller"),
    path('addtocart/<int:rid>',views.addtocart,name="addtocart"),
    path('mycart/',views.mycart,name="MyCart"),
    path('getqnty/',views.get_qnty,name="GetQty"),
    path('removeqty/<int:did>',views.removecart,name="removeqty"),
    path('payment/',views.payment,name="Payment"),
    path('viewservices/<int:vid>',views.viewservices,name="ViewServices"),
    path('searchserviceprovider/',views.searchserviceprovider,name="SearchServiceProvider"),
    path('servicebooking/<int:bid>',views.servicebooking,name="ServiceBooking"),
    path('viewservicebooking/',views.viewservicebooking,name="ViewServiceBooking"),
    path('usercomplaint/',views.usercomplaint,name="UserComplaint"),
    path('del_complaint/<int:did>',views.DeleteComplaint,name="del_complaint"),
    path('userfeedback/',views.userfeedback,name="UserFeedBack"),
    path('del_feedback/<int:did>',views.DeleteFeedback,name="del_feedback"),
    path('shopstar/<int:mid>',views.starrating,name="shoprating"),
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('ajaxserviceprovider/',views.ajaxserviceprovider,name="ajaxserviceprovider"),
    path('ajaxseller/',views.ajaxseller,name="ajaxseller"),
    path('bill/',views.bill,name="bill"),
     path('logout/',views.logout,name="logout"),
    

]    