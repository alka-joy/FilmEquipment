from django.urls import path
from Admin import views


app_name='Admin'
urlpatterns = [
    path('district/',views.dis,name="District"),
    path('del_district/<int:did>',views.DeleteDistrict,name="del_district"),
    path('edit_district/<int:eid>',views.EditDistrict,name="edit_district"),
    path('place/',views.pl,name="Place"),
    path('del_place/<int:did>',views.DeletePlace,name="del_place"),
    path('service/',views.ser,name="Service"),
    path('del_service/<int:did>',views.DeleteService,name="del_service"),
    path('edit_service/<int:eid>',views.EditService,name="edit_service"),
    path('complaint/',views.com,name="Complaint"),
    path('del_complaint/<int:did>',views.DeleteComplaint,name="del_complaint"),
    path('edit_complaint/<int:eid>',views.EditComplaint,name="edit_complaint"),
    path('category/',views.cat,name="Category"),
    path('del_category/<int:did>',views.DeleteCategory,name="del_category"),
    path('edit_category/<int:eid>',views.EditCategory,name="edit_category"),
    path('newshop/',views.shop,name="NewShop"),
    path('viewnewseller/',views.sellerlist,name="ViewNewSeller"),
    path('acceptedsellerlist/',views.acceptedsellerlist,name="AcceptedSellerList"),
    path('rejectedsellerlist/',views.rejectedsellerlist,name="RejectedSellerList"),
    path('acceptedseller/<int:aid>',views.acceptseller,name="acceptseller"),
    path('rejectedseller/<int:rid>',views.rejectseller,name="rejectseller"),
    path('adminhome/',views.adminhome,name="AdminHome"),
    path('viewsellercomplaint/',views.viewsellercomplaint,name="ViewSellerComplaint"),
    path('viewusercomplaint/',views.viewusercomplaint,name="ViewUserComplaint"),
    path('viewuserfeedback/',views.viewuserfeedback,name="ViewUserFeedback"),
    path('viewsellerfeedback/',views.viewsellerfeedback,name="ViewSellerFeedback"),
    path('logout/',views.logout,name="logout"),
    
]