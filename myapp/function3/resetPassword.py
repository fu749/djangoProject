from myapp.dao.jdbc import oracleWork, oracle_execute_query


# 重置密码操作
def resetPassword_t(a):
    procedure_name = 'Reset_passwordUser'
    params = [a]

    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result

def nowPassword_t(rname):
    query = "SELECT RD_PASSWD FROM reader WHERE rd_name = :rname"
    params = {'rname': rname}

    # 调用执行查询函数
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results[0][0]
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None