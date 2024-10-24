from myapp.dao.jdbc import oracleWork

# 分页获取书籍信息
def paging_t():
    procedure_name = 'fenye'
    params = [1, 10]  # 获取第1页，每页10条记录
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result

