from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from function1.loginOut import loginOut_t


def loginOut(request):
    result=loginOut_t()
    if result!="用户名或密码错误请重试":
        print("登出成功")
        return redirect('login')  # 登出成功后返回登录界面
    else:
        print(result)
        return render(request, 'index.html', {'error': result})
