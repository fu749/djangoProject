from myapp.dao.jdbc import oracleWork

def look_blacklist_t():
    procedure_name = 'look_blacklist'
    params = []  # 无需输入参数
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
