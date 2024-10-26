# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from sympy.printing.tree import print_node

from borrowBooks.borrow import borrow_t

@require_POST
def borrow_Book(request, book_id):  # 参数名修改为 book_id
    user = request.user
    book = borrow_t(book_id)  # 假设借书函数可以处理 book_id

    if book == "图书不存在，请联系管理员添加图书":
        print(1)
        return JsonResponse({'message': '图书不存在，请联系管理员添加图书！'}, status=200)
    elif book == "图书库存不足":
        print(2)
        return JsonResponse({'message': '图书库存不足！'}, status=200)
    elif book == "这本书你已经借过了，请先归还":
        return JsonResponse({'message': '这本书你已经借过了，请先归还!'}, status=200)
    elif book == "你已经是黑名单了，请联系管理员处理":
        return JsonResponse({'message': '你已经是黑名单了，请联系管理员处理!'}, status=200)
    elif book == "未登录请先登录":
        return JsonResponse({'message': '未登录请先登录!'}, status=200)
    else:
        print(3)
        return JsonResponse({'message': f'成功借阅{book}！'},status=200)

