"""testweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from apptest import views as apptest_views  
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^app/', apptest_views.index),
    url(r'^zn/', apptest_views.zn),
    url(r'^login/', apptest_views.login),
    url(r'^person/', apptest_views.person),
    url(r'^education/', apptest_views.education),
    url(r'^blog/', apptest_views.blog),
    url(r'^about/', apptest_views.about),
]
