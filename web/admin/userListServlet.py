from django.core.paginator import Paginator
from django.http import JsonResponse

from ROOT.user_list import user_list, black_list


def userList(request):
    user = user_list()
    sorted_data = sorted(user, key=lambda x: x[0])
    user = sorted_data
    black = black_list()
    result = [item[0] for item in black]
    user_data = []
    for cid,username, password in user:

        if username in result:
            user_data.append({
                'uid':cid,
                'username': username,
                'password': password,
                'is_blacklisted': 1
            })
        else:
            user_data.append({
                'uid': cid,
                'username': username,
                'password': password,
                'is_blacklisted': 0
            })

    page = request.GET.get('page', 1)

    # 每页10条数据
    paginator = Paginator(user_data, 10)
    users_page = paginator.get_page(page)
    # 返回当前页的数据
    return JsonResponse({
        'users': list(users_page),
        'total_pages': paginator.num_pages,
        'current_page': users_page.number
    })


