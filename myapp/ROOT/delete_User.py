from myapp.dao.jdbc import oracleWork

def deleteUser(rid):
    # 重置密码操作
    procedure_name = 'Delete_user'  # 存储过程名称
    params = [rid]  # 输入参数：新密码和用户名

    # 调用存储过程并获取结果
    output_result = oracleWork(procedure_name, params)

    # 如果有结果，打印输出
    if output_result is not None:
        return output_result
