import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from function3.resetPassword import nowPassword_t, resetPassword_t

@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        # 获取请求中的 JSON 数据
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'message': '无效的 JSON 格式'}, status=400)

        user = data.get('user')
        current_password = data.get('current_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        # 验证传入数据的完整性
        if not user or not current_password or not new_password or not confirm_password:
            return JsonResponse({'success': False, 'message': '所有字段均为必填项'})

        # 验证新密码和确认密码一致性
        if new_password != confirm_password:
            return JsonResponse({'success': False, 'message': '新密码和确认密码不一致'})

        # 获取当前密码
        password = nowPassword_t(user)

        if password is None:
            return JsonResponse({'success': False, 'message': '用户不存在或密码错误'})

        # 验证当前密码是否正确
        if str(current_password) != str(password):
            print(f"当前密码: {current_password} 用户密码: {password}")
            return JsonResponse({'success': False, 'message': '当前密码错误'})

        # 调用重置密码函数
        reset_result = resetPassword_t(new_password)
        if reset_result:
            return JsonResponse({'success': True, 'message': '密码修改成功'})
        else:
            return JsonResponse({'success': False, 'message': '密码修改失败，请稍后再试'})

    return JsonResponse({'message': '请求方式错误'}, status=405)
