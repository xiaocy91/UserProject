from django.shortcuts import render
from django.http import  HttpResponse

from usermnge.models import SysAdmin, GenrAdmin , NmlUser


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "usermnge/login.html", {})
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #首先查看SysAdmin系统管理员表
        sadmin  = SysAdmin.objects.filter( name= email )[0]
        if sadmin:
            print("%s系统管理员，登录成功" % email)
            return  HttpResponse("ok")
        else:
            print("%s系统管理员，登录失败" % email)
            return  HttpResponse()


