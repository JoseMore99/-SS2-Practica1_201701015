
import pyodbc
from dotenv import load_dotenv
import os
load_dotenv()
# Especifica el nombre del servidor, la base de datos, el nombre de usuario y la contraseña.
server = os.getenv("DB_HOST")
database =os.getenv("DB_database")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


# Establece la cadena de conexión.
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def get_conection():
    return pyodbc.connect(connection_string)

def query(quer:str, data= None):
    conexion = get_conection()

    cursor = conexion.cursor()
 
    if data:
        cursor.execute(quer,data)
    else:
        cursor.execute(quer)
    conexion.commit()
    cursor.close()
    conexion.close()

def query_conectado(conexion,quer:list, data= None ):

    cursor = conexion.cursor()
    
    for i in quer:
        print(i)
        if data:
            cursor.execute(i,data)
        else:
            cursor.execute(i)
        conexion.commit()
    cursor.close()

def query_retorno(conexion,quer:list, data= None ):

    cursor = conexion.cursor()
    retorno = None
    for i in quer:
        print(i)
        if data:
            cursor.execute(i,data)
        else:
            cursor.execute(i)
        conexion.commit()
        retorno= cursor.fetchall()
    cursor.close()
    return retorno