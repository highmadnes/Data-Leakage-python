from django.conf.urls import include, url
from django.contrib import admin
from dataApp.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home/', home, name='home'),
    url(r'^tologin/', tologin, name='tologin'),
    url(r'^toregister/', toregister, name='toregister'),
    url(r'^toadminhome/', toadminhome, name='toadminhome'),
    url(r'^toupload/', toupload, name='toupload'),
    url(r'^tosendrequest/', tosendrequest, name='tosendrequest'),
    url(r'^toview/', toview, name='toview'),
    url(r'^toblock/', toblock, name='toblock'),
    url(r'^touserhome/', touserhome, name='touserhome'),
    url(r'^operatorhome/', operatorhome, name='operatorhome'),
    url(r'^touserview/', touserview, name='touserview'),
    url(r'^tohome/', tohome, name='tohome'),
    url(r'^toleakdata/', toleakdata, name='toleakdata'),
    url(r'^register/', register, name='register'),
    url(r'^login/', login, name='login'),
    url(r'^upload/', upload, name='upload'),
    url(r'^download/', download, name='download'),
    url(r'^leak/', leak, name='leak'),
    url(r'^request/',requestss, name='request'),
    url(r'^searchid/',searchid, name='searchid'),
    url(r'^sender/',sender, name='sender'),
    url(r'^viewer/',viewer, name='viewer'),
    url(r'^block/',block, name='block'),
]
