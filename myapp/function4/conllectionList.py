from myapp.dao.jdbc import oracleWork

# 显示收藏列表
def conllectionList_t():
    procedure_name = 'Display_collection_table'  # 存储过程名称
    params = []  # 不需要输入参数

    # 调用存储过程并获取结果
    output_result = oracleWork(procedure_name, params)

    # 如果有结果，打印输出
    if output_result is not None:
        return output_result
