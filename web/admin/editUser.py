from http.client import responses

from django.shortcuts import render

from ROOT.user_list import black_list
from function1.userService import user_Name


def editUser(request):
    user_id = request.GET.get('id')
    user = user_Name(user_id)
    black = black_list()
    result = [item[0] for item in black]
    username = user[0]
    password = user[1]
    state = 0
    if username in result:
        state = 1

    responses_data = {
        "id": user_id,
        "username": username,
        "password": password,
        "state": state
    }
    return render(request, 'admin/editUser.html',responses_data)  # 渲染 index.html 模板