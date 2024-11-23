# main.py

from myapp.dao.jdbc import oracleWork, oracle_execute_query


def searchBook_t(a):
    procedure_name = 'searchbook'
    params = [a]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result

def searchBook_s(bookName):
    query = "SELECT * FROM books where book_name like :book"
    params = {"book": "%"+bookName+"%"}
    results = oracle_execute_query(query, params)
    results = sorted(results, key=lambda x: x[0])
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None
print(searchBook_s(""))
def searchBook_id(bid):
    query = "SELECT * FROM books where book_id = :bid"
    params = {"bid":bid}
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results[0]
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None

def addBook_id():
    query = "SELECT book_id FROM books"
    params = {}
    booksId = oracle_execute_query(query, params)
    results = [item[0] for item in booksId]
    result=0
    for i in range(1,10000):
        if i not in results:
            result = i
            break

    return result
