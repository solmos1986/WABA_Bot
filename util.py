import requests
import json
import actions
import os

def Registro(codLock, number):
    #AQUI RECIBO EL MESSAGE, LO SEPARO Y VERIFICO QUE SE IGUAL A:
    print("LLEGUE UTIL.Registro")
    query_getApi="SELECT a.api_url AS url FROM building b INNER JOIN api_integration a ON a.building_id = b.building_id WHERE b.code='"+codLock+"';"
    api_app=actions.DbLockConn(query_getApi) 
    query_getUserLock= "SELECT u.name AS name, u.celular AS celular, d.name, b.name, b.code FROM user u INNER JOIN department d ON u.department_id = d.department_id INNER JOIN building b ON d.building_id = b.building_id WHERE b.code='"+codLock+"';"
    users_lock=actions.DbLockConn(query_getUserLock)
    #users_app=actions.GetUsersAPP(api_app)
    
    #comparamos si los numeros de la API estan la BD del LockSoft si no los agregamos uno a uno LockId, AptoId, Nombre, Celular,Estado
    
    return api_app

def GetUrl(number):
    url_api=actions.GetUrl()
    return

def Files():
    url_img="https://i.postimg.cc/wvxfJ5Z4/100002-qr.png"
    respuesta=requests.get(url_img)
    if respuesta.status_code==200:
        print("200")
        ruta_guardado="/imagenes_qr"
        print("ruta ok")
        with open(ruta_guardado,'wb') as f:
            f.write(respuesta.content)
        print("imagen guardada")
    else:
        print("Error al descargar la imagen:",respuesta.status_code)
    return

def VerFiles():
    ruta="/images"
    files=str(os.listdir(ruta))
    print(files)
    return files