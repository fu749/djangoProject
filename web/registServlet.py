from django.shortcuts import render, redirect

from function1.regist import regist_t


def regist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result=regist_t(username, password)
        print(result)
        if result=="注册成功":
            return redirect('login')  # 登录成功后重定向到主页
        else:
            # 处理错误
            return render(request, 'regist.html', {'error': result})
    return render(request, 'regist.html')  # GET请求时显示登录页面
