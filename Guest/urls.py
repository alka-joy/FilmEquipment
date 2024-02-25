from django.urls import path
from Guest import views


app_name='Guest'
urlpatterns = [
    path('newuser/',views.user,name="NewUser"),
    path('newseller/',views.seller,name="NewSeller"),
    path('ajaxplace/',views.ajaxplace,name="AjaxPlace"),
    path('login/',views.login,name="Login"),
    path('',views.index,name="index"),
    path('serviceprovider/',views.serviceprovider,name="ServiceProvider"),
    
]