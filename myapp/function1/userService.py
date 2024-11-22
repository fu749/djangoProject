from dao.jdbc import oracle_execute_query


def user_Name(rid):
    query = "SELECT rd_name,rd_passwd FROM reader WHERE rd_id  = :rid"
    params = {'rid': rid}

    # 调用执行查询函数
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results[0]
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None