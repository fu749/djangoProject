from django.shortcuts import render
from datetime import datetime, timedelta

from borrowBooks.lookBorrowBook import lookBorrowBook
from function1.loginName import rd_online

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
                    borrow_date_str = book_info['借书时间']  # 借书时间字符串
                    try:
                        # 假设日期格式为 "YYYY-MM-DD HH:MM:SS"
                        borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d %H:%M:%S")
                        current_date = datetime.now()

                        # 计算剩余时间，假设借阅期限为 7 天
                        deadline = borrow_date + timedelta(days=7)
                        remaining_time = (deadline - current_date).days  # 剩余天数

                        # 如果剩余天数小于 0，表示已经过期
                        if remaining_time < 0:
                            remaining_time = 0

                        # 添加到书籍信息中
                        book_info_list.append({
                            'name': book_info['图书ID'],
                            'borrowDate': borrow_date_str,
                            'remainingTime': remaining_time,  # 剩余时间（天）
                        })
                    except ValueError:
                        # 如果日期格式不正确，跳过此条记录
                        continue

        # 格式化响应数据
        response_data = {
            'results': book_info_list,
        }
        return render(request, 'bookList.html', {'user': user, 'books': response_data['results']})
