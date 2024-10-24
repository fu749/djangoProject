# main.py

from myapp.dao.jdbc import oracleWork
def searchBook_t(a):
    procedure_name = 'searchbook'
    params = [a]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result