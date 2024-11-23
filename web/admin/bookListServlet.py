from django.core.paginator import Paginator
from django.http import JsonResponse

from ROOT.user_list import user_list, black_list
from function2.searchBook import searchBook_s


def bookList(request):
    query = request.GET.get('query', '').strip()
    books = searchBook_s(query)
    books_data=[]
    for book in books:
        books_data.append({
            'bookId':book[0],
            'bookName': book[1],
            'author': book[2],
            'bookNum': book[3]
        })
    page = request.GET.get('page', 1)

    # 每页10条数据
    paginator = Paginator(books_data, 10)
    books_page = paginator.get_page(page)
    # 返回当前页的数据
    return JsonResponse({
        'books': list(books_page),
        'total_pages': paginator.num_pages,
        'current_page': books_page.number
    })


