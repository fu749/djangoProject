from django.shortcuts import render


def change_user(request):
    return render(request, 'admin/editUser.html')  # 渲染 index.html 模板