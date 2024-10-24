import oracledb

def oracleWork(procedure_name, params):
    dsn = "(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=orcl)))"
    oracledb.init_oracle_client(lib_dir=r"D:\app\xuan\product\11.2.0\dbhome_1\bin")

    username = 'scott'
    password = '123456'

    try:
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        cursor = connection.cursor()

        # 定义输出参数
        result_message = cursor.var(oracledb.STRING)

        # 调用存储过程
        cursor.callproc(procedure_name, params + [result_message])

        # 提交事务
        connection.commit()

        return result_message.getvalue()  # 返回输出参数的值

    except Exception as e:
        print(f"错误: {e}")
        connection.rollback()  # 回滚事务
    finally:
        try:
            cursor.close()
        except Exception as close_e:
            print(f"关闭光标时出错: {close_e}")
        try:
            connection.close()
        except Exception as close_e:
            print(f"关闭连接时出错: {close_e}")

# 示例调用

