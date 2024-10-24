from myapp.dao.jdbc import oracleWork

# 修改或添加图书信息
def changeBook_t(id , bname , author ,number):
    procedure_name = 'change_book'  # 存储过程名称
    #params = [1, '新书名', '作者名', 10]  # 输入参数：图书ID, 图书名, 作者, 数量
    params = [id, bname, author, number]
    # 调用存储过程并获取结果
    output_result = oracleWork(procedure_name, params)

    # 如果有结果，打印输出
    if output_result is not None:
         return output_result
