from django.shortcuts import render


def adminMain(request):
    return render(request, 'admin/index.html')
