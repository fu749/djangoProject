import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ROOT.delete_Book import deleteBook
from ROOT.join_blacklist import join_blacklist_t


@csrf_exempt
def batchDeleteBook(request, book_id):
    result = deleteBook(book_id)

    if result == "没有登录不能操作" or result == "没有权限":
        return JsonResponse({'success': False, 'message': '没有权限'})
    if result == "操作失败：用户不存在":
        return JsonResponse({'success': False, 'message': '用户不存在'})
    return JsonResponse({'success': True, 'message': result})

@csrf_exempt
def batchDeleteBooks(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            book_ids = body.get('book_ids', [])
            for book_id in book_ids:
                result = deleteBook(book_id)
                if result == "没有登录不能操作" or result == "没有权限":
                    return JsonResponse({'success': False, 'message': '没有权限'})

            return JsonResponse({'success': True, 'message': '成功将选中的用户删除'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'服务器错误: {str(e)}'}, status=500)

    return JsonResponse({'success': False, 'message': '只支持 POST 请求'}, status=405)