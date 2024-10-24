from django.http import HttpResponse
from django.shortcuts import render  # 导入 render 函数

def index(request):
    # 这里可以进行逻辑处理，比如获取数据、渲染模板等
    return render(request, 'index.html')  # 渲染 index.html 模板