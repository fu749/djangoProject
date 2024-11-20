from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from borrowBooks.returnBooks import returnBooks


@require_POST
def return_Books(request, book_name):
    # 调用还书逻辑
    result = returnBooks(book_name)

    # 设置消息
    if result == "还书成功，已超时":
        messages.success(request, f'书籍 {book_name} 已成功归还，但您已超时。')
    elif result == "还书成功，按时还书":
        messages.success(request, f'书籍 {book_name} 已成功按时归还。')
    else:
        messages.error(request, '还书失败，请稍后再试。')

    # 重定向回书籍列表页面
    return redirect('book_list')  # 确保 'book_list' 是书籍列表页面的名称
