from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ROOT.delete_User import deleteUser


@csrf_exempt
def delete_user(request, user_id):
    result = deleteUser(user_id)

    if result == "没有登录不能操作" or result == "没有权限":
        return JsonResponse({'success': False, 'message': '没有权限'})
    if result == "操作失败：用户不存在":
        return JsonResponse({'success': False, 'message': '用户不存在'})
    return JsonResponse({'success': True, 'message': result})
