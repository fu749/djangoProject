from django.shortcuts import render


def loginAdmin(request):
    return render(request, 'admin/login.html')

def admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username!="root" and password!="123456"):
            return render(request, 'admin/login.html')
    return render(request, 'admin/index.html')
