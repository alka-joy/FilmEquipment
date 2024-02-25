from django.urls import path
from ServiceProvider import views

app_name='ServiceProvider'

urlpatterns = [

    path('serviceproviderhome/',views.serviceproviderhome,name="ServiceProviderHome"),
    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofile/',views.editprofile,name="EditProfile"),
    path('changepassword/',views.changepassword,name="ChangePassword"),
    path('services/',views.services,name="Services"),
    path('del_services/<int:did>',views.DeleteServices,name="del_services"),
    path('edit_services/<int:eid>',views.EditServices,name="edit_services"),
    path('viewbooking/',views.viewbooking,name="ViewBooking"),

]