from myapp.dao.jdbc import oracleWork

def borrow_t(a):
    procedure_name = 'Borrow'
    params = ["《"+a+"》"]  # 传递书名
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
