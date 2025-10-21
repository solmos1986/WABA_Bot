#import requests
import qrcode
#import matplotlib.pyplot as plt
import json
#import mysql.connector # type: ignore
import os
from PIL import Image

def CodeConverter(code):
        print(code)
        numero=code
                # Crear instancia del QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Añadir el número como cadena
        qr.add_data(str(numero))
        qr.make(fit=True)
        
        # Crear la imagen del QR
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        print("RGB")
        tamaño_final = (300, 300)  # Puedes cambiar esto
        print("pase tamaño")
        img_resized = img.resize(tamaño_final)
        print("redimensionada")
        #guardar QR
        ruta_actual = os.path.dirname(os.path.abspath(__file__)) #"/public_html/imagenes"
        print("ruta actual :"+ruta_actual)
        archivo_qr = os.path.join(ruta_actual, f"{numero}_qr.jpg")
        img_resized.save(archivo_qr)
        retorno=str(f"{numero}_qr.jpg")
        print("URLLLL : "+retorno)
        print("archivo : "+archivo_qr)
        print("archivo2 : "+f"{numero}_qr.jpg")
        return retorno
