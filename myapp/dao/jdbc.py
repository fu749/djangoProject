import oracledb


def oracle_connect():
    """
    初始化 Oracle 客户端并返回连接配置。
    """
    dsn = "(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=orcl)))"
    oracledb.init_oracle_client(lib_dir=r"D:\app\xuan\product\11.2.0\dbhome_1\bin")

    username = 'scott'
    password = '123456'
    return username, password, dsn


def oracleWork(procedure_name, params):

    username, password, dsn = oracle_connect()

    try:
        # 建立连接
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        cursor = connection.cursor()

        # 定义输出参数
        result_message = cursor.var(oracledb.STRING)

        # 调用存储过程
        cursor.callproc(procedure_name, params + [result_message])

        # 提交事务
        connection.commit()

        # 返回输出参数的值
        return result_message.getvalue()

    except oracledb.Error as e:
        print(f"Oracle 错误: {e}")
        connection.rollback()  # 回滚事务
        return None

    except Exception as e:
        print(f"其他错误: {e}")
        return None

    finally:
        # 关闭资源
        if 'cursor' in locals() and cursor:
            try:
                cursor.close()
            except Exception as close_e:
                print(f"关闭光标时出错: {close_e}")

        if 'connection' in locals() and connection:
            try:
                connection.close()
            except Exception as close_e:
                print(f"关闭连接时出错: {close_e}")


def oracle_execute_query(query, params=None):
    username, password, dsn = oracle_connect()

    try:
        # 建立连接
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # 如果是 SELECT 查询，返回结果集
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            return results

        # 如果是非 SELECT 查询，返回受影响的行数
        connection.commit()
        return cursor.rowcount

    except oracledb.Error as e:
        print(f"Oracle 错误: {e}")
        connection.rollback()
        return None

    except Exception as e:
        print(f"其他错误: {e}")
        return None

    finally:
        # 关闭资源
        if 'cursor' in locals() and cursor:
            try:
                cursor.close()
            except Exception as close_e:
                print(f"关闭光标时出错: {close_e}")

        if 'connection' in locals() and connection:
            try:
                connection.close()
            except Exception as close_e:
                print(f"关闭连接时出错: {close_e}")
