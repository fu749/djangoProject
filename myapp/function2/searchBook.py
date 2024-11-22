# main.py

from myapp.dao.jdbc import oracleWork, oracle_execute_query


def searchBook_t(a):
    procedure_name = 'searchbook'
    params = [a]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result

def searchBook_s():
    query = "SELECT * FROM books"
    params = {}
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None