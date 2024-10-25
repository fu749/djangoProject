from django.http import JsonResponse
from function2.searchBook import searchBook_t


def search_books(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')  # 获取前端传过来的搜索参数
        results = searchBook_t(search_query)  # 调用搜索函数
        print(results)

        book_info_list = []  # 用于存储多个书籍的信息

        # 检查 results 是否为字符串并进行处理
        if isinstance(results, str):
            # 将字符串按逗号分割成不同的部分
            book_items = results.split(', ')
            book_info = {}

            for item in book_items:
                # 分割每个部分为键和值
                parts = item.split(': ', 1)  # 只分割一次
                if len(parts) == 2:  # 确保有键和值
                    key, value = parts
                    book_info[key.strip()] = value.strip()  # 存储当前书籍的信息

            # 确保 book_info 包含书名和作者
            if 'Book Name' in book_info and 'Author' in book_info:
                book_info_list.append({
                    'name': book_info['Book Name'],
                    'author': book_info['Author'],
                    'id': book_info.get('Book ID', None)  # 可选的 Book ID
                })

        # 打印所有书籍信息
        print(book_info_list)
        response_data = {'results': book_info_list}  # 格式化为字典，包含书籍列表

        return JsonResponse(response_data)  # 返回 JSON 响应
