from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static

from django.conf import settings
from . import views
urlpatterns = [
    path('',views.home , name = 'home'),
    path('register/',views.registr, name = 'register'),
    path('login/' , views.login , name = 'login'),
    path('login/d-login/' , views.dlogin , name = 'dlogin'),
    path('login/user-login/' , views.ulogin , name = 'ulogin'),
    path('login/admin-login/' , views.adminlogin , name = 'adminlogin'),
    path('register/doctor-register/',views.doctor_register,name='doctor_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)