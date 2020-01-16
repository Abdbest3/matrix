from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static

from django.conf import settings
from . import views
urlpatterns = [
    path('',views.home , name = 'home'),
    path('register/',views.registr, name = 'register'),
    path('login/' , views.login , name = 'login'),
    path('doctor-register/save-doctor/',views.doctor_register,name='doctor_register'),
    path('doctor-register/',views.doctor_register,name='doctor_register1'),
    path('register/user-register/',views.u_register,name = 'u_register'),
    path('user-register/',views.u_register,name = 'u_register1'),
    path('user-register/save-usr/',views.u_register,name = 'u_register1'),
    path('user-login/',views.ulogin,name = 'ulogin'),
    path('user-login/ulogin/',views.ulogin,name = 'ulogin1'),
    path('doctor-login/',views.dlogin,name='dlogin'),
    path('doctor-login/dlogin/',views.dlogin,name='dlogin'),
    path('user-login/ulogin/alldoctor/',views.alldoctor,name='alldoctor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)