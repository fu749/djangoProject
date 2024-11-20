from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from function4.unconllection import unconllection_t


@require_POST
def unCollection(request, book_id):
    # 调用还书逻辑
    result = unconllection_t(book_id)

    # 设置消息
    if result == "取消成功":
        messages.success(request, f'书籍 {book_id} 已从你的收藏中移除。')
    else:
        messages.error(request, '取消失败，请稍后再试。')

    # 重定向回书籍列表页面
    return redirect('Collection_List')  # 确保 'book_list' 是书籍列表页面的名称
