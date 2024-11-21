# main.py

def out_blackList_t(name):
    from myapp.dao.jdbc import oracleWork
    # 登录
    procedure_name = 'remove_blacklist'
    params = [name]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
