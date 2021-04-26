"""Dooya_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from aiohttp.web_routedef import static
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url, re_path
from django.urls import path

from Dooya_web import settings
from web_project import views
from captcha.views import captcha_refresh
from django.views.static import serve
from django.views.static import serve
from Dooya_web.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static_all'),]

    path('page.html/', views.page),
    # url(r'^page/(?P<pindex>.*)$', views.page),
    # url(r'^page/?(?P<pindex>\d+)/', views.page),
    path('', include('web_project.urls')),
    path('motorTest/', include('MotorTest_project.urls')),


    path('register/', views.register),
    path(r'captcha/', include('captcha.urls')),
    path('confirm/', views.confirm_user),
    path('log_in/', views.log_in),
    path('sign_out/', views.sign_out),
    path('captcha/refresh/', captcha_refresh),
    path('download/', views.download),
    path('download_testMotor/', views.download_testMotor),
    path('request_testMotor_version/', views.request_testMotor_version),
    path('uploadFile/', views.uploadFile),
    path('uploadFile_winform/', views.uploadFile_winform),
    path('feedback_motorTest/', views.feedback_motorTest),
]
