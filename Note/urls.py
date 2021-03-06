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
from Note import views


urlpatterns = [
    url(r'^importer_csv', views.importer_csv, name='importer_csv'),
    url(r'^suppall', views.suppall, name='suppall'),
    url(r'^listernotes', views.listernotes, name='listernotes'),
    url(r'^supprnote/(?P<id>\d+)$', views.supprnote, name='supprnote'),
    url(r'^modifierNote', views.modifierNote, name='modifierNote'),
    url(r'^resultatJury', views.resultatJury, name='resultatJury'),
    url(r'^listerResultat', views.renseignerResultat, name='renseignerResultat'),
    url(r'^completerResultat/(?P<id>\d+)/(?P<Isemestre>\d+)$', views.completerResultat, name='completerResultat'),
    
]
