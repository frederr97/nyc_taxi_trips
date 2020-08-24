# -*- coding: utf-8 -*-

import pyodbc 


# Returns a connector to Azure SQL
def sqlConnect():
    server = 'practicalserver.database.windows.net'
    database = 'PRACTICALDB' 
    username = 'SOMEONE' 
    password = 'Azuredb$!' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn