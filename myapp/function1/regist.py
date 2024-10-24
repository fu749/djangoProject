# main.py

from myapp.dao.jdbc import oracleWork
#注册
def regist_t(a,b):
    procedure_name = 'regist'
    params = [a, b]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result