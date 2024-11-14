
from django.shortcuts import render  # 导入 render 函数

from function1.loginName import rd_online


def index(request):
    # 这里可以进行逻辑处理，比如获取数据、渲染模板等
    user = rd_online()
    return render(request, 'index.html',{'user': user})  # 渲染 index.html 模板