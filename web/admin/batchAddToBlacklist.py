from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ROOT.join_blacklist import join_blacklist_t
from ROOT.out_balckList import out_blackList_t


@csrf_exempt
def batch_add_blacklist(request):
    if request.method == 'POST':
        try:
            # 解析 JSON 数据
            body = json.loads(request.body)
            user_names = body.get('user_name', [])
            print(user_names)
            for user_name in user_names:
                result = join_blacklist_t(user_name)
                if result == "没有登录不能操作" or result == "没有权限":
                    return JsonResponse({'success': False, 'message': '没有权限'})
            return JsonResponse({'success': True, 'message': '成功将选中的用户拉入黑名单'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'服务器错误: {str(e)}'}, status=500)

    return JsonResponse({'success': False, 'message': '只支持 POST 请求'}, status=405)


@csrf_exempt
def batch_Remove_Blacklist(request):
    if request.method == 'POST':
        try:
            # 解析 JSON 数据
            body = json.loads(request.body)
            user_names = body.get('user_name', [])
            print(user_names)
            for user_name in user_names:
                result = out_blackList_t(user_name)
                if result == "没有登录不能操作" or result == "没有权限":
                    return JsonResponse({'success': False, 'message': '没有权限'})
            return JsonResponse({'success': True, 'message': '成功将选中的用户拉入黑名单'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'服务器错误: {str(e)}'}, status=500)

    return JsonResponse({'success': False, 'message': '只支持 POST 请求'}, status=405)