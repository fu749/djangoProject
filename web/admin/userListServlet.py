from django.http import JsonResponse

from ROOT.user_list import user_list,balck_list


def search_books():
    user = user_list()
    black = balck_list()
    result = [item[0] for item in black]
    for i in user:
        if i[0] in result:
            print(i)
    response_data = {
        'username'
    }
    # return JsonResponse(response_data)

search_books()
