from myapp.dao.jdbc import oracleWork

# 收藏操作
def conllection_t(id):
    procedure_name = 'collection'  # 存储过程名称
    params = [id]

    # 调 用存储过程并获取结果
    output_result = oracleWork(procedure_name, params)

    # 如果有结果，打印输出
    if output_result is not None:
        return output_result
