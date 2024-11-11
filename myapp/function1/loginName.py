from myapp.dao.jdbc import oracleWork
def rd_online():
    procedure_name = 'rd_onlineL'

    params = []
    output_result = oracleWork(procedure_name, params)
    if output_result is not None:
        return output_result
