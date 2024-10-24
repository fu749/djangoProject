
from myapp.dao.jdbc import oracleWork
# 登录
def loginOut_t():
    procedure_name = 'logout'
    params = []  # 无需输入参数
    output_result = oracleWork(procedure_name, params)
    print(output_result)
    if output_result is not None:
        return output_result

loginOut_t()