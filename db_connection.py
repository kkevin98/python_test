'''
    Funzione che si connette ad un database.
    Uso dei parametri Keyword=value.
'''
def db_con (**option):
    con_parameters = {
        'host': option.get('host', '122. 0. 13. 2'),
        'port': option.get('port', '5432'),
        'user': option.get('user', ''),
        'password': option.get('password', ''),
    }
    print(con_parameters)
db_con()
db_con(host='130. 120. 110. 2')

