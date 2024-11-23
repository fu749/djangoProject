# main.py
from myapp.dao.jdbc import oracleWork
def changeBook(bid, name, author, num):
    procedure_name = 'change_book'
    params = [bid, name, author, num]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
