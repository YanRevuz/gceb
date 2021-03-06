"""cursusEtu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from Diplome import views


urlpatterns = [
   # url(r'^ajouterDiplome', views.ajouterDiplome, name='ajouterDiplome'),
    url(r'^listerDiplomes', views.listerDiplomes, name='listerDiplomes'),
    url(r'^ajouterDiplome', views.ajouterDiplome, name='ajouterDiplome'),
	#url(r'^ajouterDiplomeCreation/(?P<annee>\d+)$', views.ajouterDiplomeCreation, name='ajouterDiplomeCreation'),
    url(r'^supprdip/(?P<id>\d+)$', views.supprdip, name='supprdip'),
    url(r'^modifierDiplome', views.modifierDiplome, name='modifierDiplome'),
    url(r'^detailDiplome', views.detailDiplome, name='detailDiplome'),
]
