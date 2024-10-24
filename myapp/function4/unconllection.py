from myapp.dao.jdbc import oracleWork

def unconllection_t(a):
    # 取消收藏操作
    procedure_name = 'Cancel_collection'  # 存储过程名称
    params = [a]

    # 调用存储过程并获取结果
    output_result = oracleWork(procedure_name, params)

    # 如果有结果，打印输出
    if output_result is not None:
        return output_result
