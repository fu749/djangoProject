import json

from django.http import JsonResponse
from django.shortcuts import render

from ROOT.join_blacklist import join_blacklist_t
from ROOT.out_balckList import out_blackList_t
from ROOT.resetPassword import resetPassword_t


def saveUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userId = data.get('userId')
        username = data.get('username')
        password = data.get('password')
        blacklist_status = data.get('blacklistStatus')
        result = resetPassword_t(password,username)
        if result == "没有登录不能操作" or result == "没有权限":
            return JsonResponse({'success': False, 'message': '没有权限'})
        if result == "操作失败：用户不存在":
            return JsonResponse({'success': False, 'message': '用户不存在'})

        if blacklist_status == '0':
            out_blackList_t(username)
        else:
            join_blacklist_t(username)

        return JsonResponse({'success': True, 'message': '用户信息改变成功'})