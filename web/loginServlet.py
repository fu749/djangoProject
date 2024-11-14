from django.shortcuts import render, redirect

from function1.login import login_t
from function1.loginName import rd_online
from function1.loginOut import loginOut_t


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        loginOut_t()
        result=login_t(username, password)
        print(result)
        if result==f"{username} 登录成功":
            user = rd_online()
            return render(request, 'index.html',{'user': user})   # 登录成功后重定向到主页
        else:
            # 处理错误
            return render(request, 'login.html', {'error': result})
    return render(request, 'login.html')  # GET请求时显示登录页面
