from myapp.dao.jdbc import oracleWork

# 重置密码操作
def resetPassword_t(a):
    procedure_name = 'Reset_passwordUser'
    params = [a]

    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
