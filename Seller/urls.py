from django.urls import path
from Seller import views

app_name='Seller'

urlpatterns = [
    path('sellerhome/',views.sellerhome,name="SellerHome"),
    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofile/',views.editprofile,name="EditProfile"),
    path('changepassword/',views.changepassword,name="ChangePassword"),
    path('productgallery/',views.productgallery,name="ProductGallery"),
    path('rentitem/',views.rentitem,name="RentItem"),
    path('del_rentitem/<int:did>',views.DeleteRentItem,name="del_rentitem"),
    path('sellercomplaint/',views.sellercomplaint,name="SellerComplaint"),
    path('del_complaint/<int:did>',views.DeleteComplaint,name="del_complaint"),
    
]