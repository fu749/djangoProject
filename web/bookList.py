from django.http import JsonResponse
from django.shortcuts import render

from borrowBooks.lookBorrowBook import lookBorrowBook
from function1.loginName import rd_online
from function2.searchBook import searchBook_t

def Book_List(request):
    user = rd_online()
    if request.method == 'GET':
        results = lookBorrowBook()

        book_info_list = []  # 用于存储多个书籍的信息

        # 将字符串解析为书籍信息列表
        if isinstance(results, str):
            book_items = results.strip().split('\n')  # 按行分割
            for item in book_items:
                book_info = {}
                parts = item.split(', ')  # 按逗号分割每行内容
                for part in parts:
                    key_value = part.split(': ', 1)  # 只分割一次
                    if len(key_value) == 2:  # 确保有键和值
                        key, value = key_value
                        book_info[key.strip()] = value.strip()  # 存储当前书籍的信息

                # 确保包含书名和借阅日期
                if '图书ID' in book_info and '借书时间' in book_info:
                    book_info_list.append({
                        'name': book_info['图书ID'],
                        'borrowDate': book_info['借书时间'],
                    })


        # 格式化响应数据
        response_data = {
            'results': book_info_list,
        }
        print(response_data)
        return render(request, 'bookList.html', {'user': user, 'books': response_data['results']})
