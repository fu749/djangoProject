import json

from django.http import JsonResponse

from ROOT.change_Book import changeBook


def updateBook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bookId = data.get('id')
        bookName = data.get('title')
        author = data.get('author')
        bookNum = data.get('stock')

        result = changeBook(bookId, bookName,author,bookNum)

        if result == "没有登录不能操作" or result == "没有权限":
            return JsonResponse({'success': False, 'message': '没有权限'})
        if result == "操作失败：用户不存在":
            return JsonResponse({'success': False, 'message': '用户不存在'})

        return JsonResponse({'success': True, 'message': result})

    return JsonResponse({'success': False, 'message': '只支持 POST 请求'}, status=405)