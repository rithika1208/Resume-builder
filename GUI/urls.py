"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from basics.views import *


urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True)), 
    path("admin/", admin.site.urls),
    path('form/', form, name='form'),        
    path('resume/', resume, name='resume'),
    path('download/', download_pdf, name='download_pdf'),
    path('download1/', download_pdf1,  name='download_pdf1'),
    path('template/', template,  name='template'),
    path('home/',home, name='home'),
    path('login/',user_login,name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',user_logout,name='logout'),
    path('form1/',form1,name='form1'),
    path('resume1/',resume1,name='resume1'),
    path('edit_resume/<int:template_id>/', edit_resume, name="edit_resume"),

]