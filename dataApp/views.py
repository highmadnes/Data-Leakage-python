from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
import random as r
from models import *
##import rabin
import hashlib
import os
# Create your views here.

def home(request):
    return render(request,"Home/index.html",{})
def tologin(request):
    return  render(request,"Home/login.html",{})
def toregister(request):
    return render(request,"Home/register.html",{"status":3})
def toadminhome(request):
    return render(request,'Admin/index2.html',{})
def toupload(request):
    ob = Registration.objects.all().exclude(role=0).exclude(role=2)
    return render(request,'Admin/Upload.html',{"users":ob})
def tosendrequest(request):
    ob=Request.objects.all()
    return render(request,"Admin/leakedhashes.html",{"data":ob})
def toview(request):
    return render(request,"Admin/view.html",{})
def toblock(request):
    ob=Registration.objects.filter(role=1)
    return render(request,"Admin/block.html",{'users':ob})
def touserhome(request):
    obj=Uploader.objects.filter(userid=request.session["userid"])
    return render(request,"User/download.html",{"data":obj,"Username":Registration.objects.get(id=request.session["userid"]).Name})
def toleakdata(request):
    obj=Uploader.objects.filter(userid=request.session["userid"])
    return render(request,"User/leak.html",{"data":obj,"Username":Registration.objects.get(id=request.session["userid"]).Name})
def tohome(request):
    return home(request)
def touserview(request):
    ob=Registration.objects.filter(role=1)
    return render(request,'Admin/viewemp.html',{"users":ob})




def register(request):
    if Registration.objects.filter(Email=request.POST.get("email")).count()>1:
        return render(request, 'Home/register.html', {"status":0})
    else:
        Registration(Name=request.POST.get("name"),Email=request.POST.get("email"),Phone=request.POST.get("number"),Date=request.POST.get("date"),Pass=request.POST.get("password"),role=1,status=1).save()
        return render(request,'Home/register.html',{"status":1})
def login(request):
    try:
        print request.POST.get("email"),request.POST.get("password")
        ob=Registration.objects.get(Email=request.POST.get("email"),Pass=request.POST.get("password"))
        if ob.role==0:
            return render(request,"Admin/index2.html",{})
        elif ob.role==1:
            if ob.status==0:
               return HttpResponse("<script>alert('You are Blocked.Please contact admin');window.location.href='/home/';</script>")
            request.session["userid"]=ob.id
            obj=Uploader.objects.filter(userid=request.session["userid"])
            return render(request,"User/download.html",{"data":obj,"Username":ob.Name})
        elif ob.role==2:
            obx=Request.objects.all().exclude(status=0)
            return render(request, "operator.html", {"data":obx})
    except Exception,e:
        print e.args,e.message
##        return render(request,"Home/login.html",{})
	return HttpResponse("<script>alert('Invalid Username or Password');window.location.href='/tologin/';</script>")
def upload(request):
    f=request.FILES["file"]
    name=""
    for i in range(0,10):
        name=name+str(r.randrange(0,9))
    name=name+str(os.path.splitext(f.name)[1])
    print name
    fs=FileSystemStorage("dataApp/uploads")
    fs.save(name,f)
    obj=Uploader(Filename=name,userid=int(request.POST.get("userid")),fingerprint=name,status=0)
    obj.save()
    h = hashlib.sha256()
    with open("dataApp/uploads/"+name,"rb",buffering=0) as fl:
        for i in iter(lambda :fl.read(128*1024),b''):
            h.update(i)
    hashvalue=h.hexdigest()
    obj.fingerprint=hashvalue
    obj.save()
    ob = Registration.objects.all().exclude(role=0).exclude(role=2)
    return render(request,'Admin/Upload.html',{"users":ob})
def download(request):
    ob=Uploader.objects.get(id=request.POST.get("id"))
    ob.status=1
    ob.save()
    with open("dataApp/uploads/"+request.POST.get("fname"), 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' +request.POST.get("fname")
        return response
    return response
def leak(request):
    ob=Request(rabin=request.POST.get("hash"),userid="",checked=0,status=0)
    ob.save()
    return toleakdata(request)
def requestss(requests):
    ob=Request.objects.get(rabin=requests.POST.get("hash"))
    ob.status=1
    ob.save()
    return  tosendrequest(requests)
def searchid(request):
    ob=Uploader.objects.filter(fingerprint=request.GET.get("hashv")).last()
    return HttpResponse(str(ob.userid))
def sender(request):
    print request.GET.get("idd"),request.GET.get("user")
    ob = Request.objects.get(id=request.GET.get("idd"))
    ob.userid=request.GET.get("user")
    ob.checked=1
    ob.save()
    print "ok"
    return HttpResponse("Send")
def operatorhome(request):
    obx = Request.objects.all().exclude(status=0)
    return render(request, "operator.html", {"data": obx})
def viewer(request):
    ob=Registration.objects.get(id=Request.objects.get(id=request.GET.get("idd")).userid)
    return HttpResponse(str(ob.Name))
def block(request):
    ob=Registration.objects.get(id=request.POST.get("id"))
    ob.status=request.POST.get("status")
    ob.save()
    return toblock(request)

