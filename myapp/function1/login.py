# main.py
from django.contrib.auth.password_validation import password_changed

from myapp.dao.jdbc import oracleWork
def login_t(a , b):
    procedure_name = 'login'
    #params = ["a", "12345"]

    params = [a, b]
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
