from django.shortcuts import render

from function1.login import login_Admin


def loginAdmin(request):
    return render(request, 'admin/login.html')

def admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result = login_Admin(username)
        if result is not None and str(result) == password :
            return render(request, 'admin/index.html')
    return render(request, 'admin/login.html')

