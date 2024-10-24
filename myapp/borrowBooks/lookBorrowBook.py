from myapp.dao.jdbc import oracleWork

def lookBorrowBook():
    procedure_name = 'look_borrow'
    params = []  # 无需输入参数
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
