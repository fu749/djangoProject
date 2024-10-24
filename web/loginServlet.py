from django.shortcuts import render, redirect

from function1.login import login_t


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result=login_t(username, password)
        print(result)
        if result==f"{username} 登录成功":
            return redirect('index')  # 登录成功后重定向到主页
        else:
            # 处理错误
            return render(request, 'login.html', {'error': result})
    return render(request, 'login.html')  # GET请求时显示登录页面
