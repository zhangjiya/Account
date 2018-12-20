from django.shortcuts import render_to_response
from account_web.UserManager import usermanager
from django.http.response import HttpResponse
import
# Create your views here.

# 主页
class LOIN:
    def __init__(self):
        self.usermanage = usermanager()
    def login(self,reque):
        # 进入界面返回登录页
        if reque.method == "Get":
            return render_to_response('login.html')
        else:
        #提交登录界面，校验用户密码
            username = request.POST.get("username")
            password = request.POST.get("password")
        if self.usermanage.has_key(username):
            if self.usermanage[username] == password:
                # 进入主页面
                return render_to_response("index.html")
            # else:
            #     return HttpResponse("用户名或密码错误")
        else:
            return HttpResponse("用户名或密码错误")



