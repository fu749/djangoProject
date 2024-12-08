from django.http import JsonResponse
from function2.searchBook import searchBook_t


def search_books(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')  # 获取前端传过来的搜索参数
        page = int(request.GET.get('page', 1))  # 获取当前页码，默认是1
        page_size = int(request.GET.get('pageSize', 10))  # 获取每页显示的记录数，默认是10

        results = searchBook_t(search_query)  # 调用搜索函数

        book_info_list = []  # 用于存储多个书籍的信息

        # 检查 results 是否为字符串并进行处理
        if isinstance(results, str):
            # 将字符串按行分割成不同的部分
            book_items = results.strip().split('\n')  # 按行分割
            for item in book_items:
                book_info = {}
                # 分割每个部分为键和值
                parts = item.split(', ')  # 按逗号分割每行内容
                for part in parts:
                    key_value = part.split(': ', 1)  # 只分割一次
                    if len(key_value) == 2:  # 确保有键和值
                        key, value = key_value
                        book_info[key.strip()] = value.strip()  # 存储当前书籍的信息

                # 确保 book_info 包含书名和作者
                if 'Book Name' in book_info and 'Author' in book_info:
                    book_info_list.append({
                        'name': book_info['Book Name'],
                        'author': book_info['Author'],
                        'id': book_info.get('Book ID', None)  # 可选的 Book ID
                    })

        # 计算分页信息
        total_count = len(book_info_list)  # 总记录数
        total_pages = (total_count + page_size - 1) // page_size  # 向上取整得到总页数

        # 分页处理
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        paginated_books = book_info_list[start_index:end_index]  # 获取当前页的数据

        # 格式化响应数据
        response_data = {
            'results': paginated_books,
            'totalCount': total_count,
            'totalPages': total_pages
        }

        return JsonResponse(response_data)  # 返回 JSON 响应
