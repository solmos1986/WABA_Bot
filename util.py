import requests
import json
import actions
import os
from PIL import Image, ImageDraw

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
    # Crear una imagen nueva (ejemplo: color sólido)
    img = Image.new('RGB', (200, 200), color='blue')

    # Dibujar en la imagen si quieres añadir contenido
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Hola", fill=(255,255,0))

    # Especificar el directorio y nombre de archivo
    ruta_directorio = "/images"
    nombre_archivo = "mi_imagen.png"
    ruta_completa = f"{ruta_directorio}/{nombre_archivo}"

    # Guardar la imagen en ese directorio
    img.save(ruta_completa)

    print(f"Imagen guardada en {ruta_completa}")
    return

def VerFiles():
    ruta="/images"
    files=str(os.listdir(ruta))
    print(files)
    return files