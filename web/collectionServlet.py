# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from function4.conllection import conllection_t


@require_POST
def collection_Book(request, book_id):  # 参数名修改为 book_id
    book = conllection_t(book_id)  # 假设借书函数可以处理 book_id

    if book == "没有登录不能操作":
        print(1)
        return JsonResponse({'message': '没有登录不能操作'}, status=200)
    elif book == "已经收藏":
        return JsonResponse({'message': '已经收藏！'}, status=200)
    elif book == "收藏成功":
        return JsonResponse({'message': '收藏成功'}, status=200)

