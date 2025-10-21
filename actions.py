import requests
import json
import mysql.connector
def GetUsersAPP(url): #AQUI CONSUMIREMOS LA API DE AMIR
    users_app=requests.get(url)
    # Verificar que la petición fue exitosa
    if users_app.status_code == 200:
        users_API = users_app.json()  # Obtener los datos en formato JSON
        print(users_API)
        return users_API
    else:
        print(f'Error en la petición: {users_app.status_code}')    
        return

def DbLockConn(query):
    print("llegue DbLockConn")
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='109.199.126.105',        # por ejemplo 'localhost'
            user='lock_app',
            password='BY5KCkxZjJrXDHdE',
            database='lock_app'
        )
        print(conexion)

        cursor = conexion.cursor()

        # Ejecutar consulta SQL
        cursor.execute(query)

        # Obtener resultados
        api = cursor.fetchall()
        for fila in api:
            print(fila)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
    return api #ver de convertir a JSON o depende como nos devuelve la info la API de AMIR para comparar

def GetUsersLock(api_url2):
    api_url=api_url2
    print("LLEGUE  SYNC BDs  "+api_url2)
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='https://109.199.126.105:887',        # por ejemplo 'localhost'
            user='lock_app',
            password='BY5KCkxZjJrXDHdE',
            database='lock_app'
        )

        cursor = conexion.cursor()

        # Ejecutar consulta SQL
        query = api_url
        cursor.execute(query)

        # Obtener resultados
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
    return resultados
# Uso del método

def GetNumbers(api_url2):
    #Aqui nos conectamos a la BD del Lock Server y buscamos el/los numeros de celular
    api_url=api_url2
    print("LLEGUE  SYNC BDs  "+api_url)
    try:
    # Conectar a la base de datos
        conexion = mysql.connector.connect(host="109.199.126.105", port="3306", user="lock_app",password="BY5KCkxZjJrXDHdE", database="lock_app")
        cursor = conexion.cursor()
        print("Con exitooo")
        id_usuario=101
        # Consulta que une dos tablas relacionadas
        cursor.execute(api_url2)
        resultados = cursor.fetchall()
        print("Con exitooo2")
        print(resultados)
        print("Con exitooo3")
            
    except mysql.connector.Error as err:
                    print("Error: ", err)
                    
    finally:
        if 'cursor' in locals():
            cursor.close()
            if 'conexion' in locals() and conexion.is_connected():
                conexion.close()
    return resultados
def InsUsersLock():
    #aqui el procedimiento de insertar datos a la BD del locker LockId, AptId, Nombre, Telefono y Estado 
    
    return

def UpdtUserLock():
    #el Estado cambiar a deshabilitado si se desconecta desde boton desvincular numero
    #ver forma de que se vuelva a vincular si cambia de opinion
    return
#api = "https://api.example.com/datos"
#resultado = obtener_datos(api)
#print(resultado)