from dao.jdbc import oracle_execute_query


def user_list(rname):
    query = "SELECT * FROM reader WHERE rd_id != :rd_id and rd_name like :rname"
    params = {"rd_id": 1,"rname": "%"+rname+"%"}
    # 调用执行查询函数
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None

def black_list():
    query = "SELECT RD_NAME FROM blacklist"
    params = {}
    # 调用执行查询函数
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None