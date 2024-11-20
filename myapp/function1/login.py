# main.py
from django.contrib.auth.password_validation import password_changed

from myapp.dao.jdbc import oracleWork, oracle_execute_query


def login_t(a , b):
    procedure_name = 'login'
    #params = ["a", "12345"]

    params = [a, b]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result


def login_Admin(rname):
    query = "SELECT RD_PASSWD FROM reader WHERE rd_id = :dept_id and rd_name = :rname"
    params = {'dept_id': 1, 'rname': rname}

    # 调用执行查询函数
    results = oracle_execute_query(query, params)
    # 进一步处理查询结果（如需要）
    if results:
        # 如果有结果，返回第一个匹配项（通常用于验证登录）
        return results[0][0]
    else:
        # 如果没有找到匹配的记录，返回 None 或空
        return None

