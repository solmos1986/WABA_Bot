from flask import Flask, request, send_from_directory
import qrconverter
import whatsappservices
import util
import actions
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from urllib.parse import urlparse, parse_qs

# Directorio donde están los archivos
DIRECTORIO = "/images"  # Cambia por tu ruta

class MiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parsear la URL
        url_parse = urlparse(self.path)
        query_params = parse_qs(url_parse.query)
        
        # Obtener el 'archivo' desde los parámetros GET
        archivo = query_params.get('archivo', [None])[0]
        
        if archivo:
            ruta_completa = os.path.join(DIRECTORIO, archivo)
            if os.path.isfile(ruta_completa):
                # Detectar MIME type según extensión
                ext = os.path.splitext(ruta_completa)[1].lower()
                if ext == '.png':
                    self.send_response(200)
                    self.send_header('Content-type', 'image/png')
                elif ext in ['.jpg', '.jpeg']:
                    self.send_header('Content-type', 'image/jpeg')
                elif ext == '.html':
                    self.send_header('Content-type', 'text/html')
                else:
                    self.send_header('Content-type', 'application/octet-stream')
                self.end_headers()
                with open(ruta_completa, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Archivo no encontrado")
        else:
            # No se pasó ningún parámetro 'archivo'
            self.send_response(400)
            self.end_headers()
            self.wfile.write("Debe especificar el parámetro 'archivo' en la URL")

app=Flask(__name__)


@app.route('/welcome/<name>',methods=['GET'])
def index(name):  
    ver_files=util.VerFiles(name)
  
    
    return ver_files

@app.route('/whatsapp',methods=['GET'])
def VerifyToken():
    try:
        accessToken="78ACCESSTOKENAPLUS78HH78"
        token=request.args.get("hub.verify_token")
        challenge=request.args.get("hub.challenge")
        if token!=None and challenge!=None and token==accessToken:
            return "TOKEN VERIFICADO" + challenge
        else:
            return "", 400
    except:
        return "",400
@app.route('/whatsapp',methods=['POST'])
def ReceivedMessage():
        print("llegeeee whba")
        #Aqui debo identificar si el mensaje viene del QR voy a metodo numberverificator.QrSync BD_usuarios
        #NO viene de QR envío el número de teléfono a metodo numberverificator.verificarRegistro a verificar si está en BD del Casillero
        #Si el retorno es TRUE 
        try:
            body=request.get_json()
            entry=(body["entry"])[0]
            changes=(entry["changes"])[0]
            value=changes["value"]
            message=(value["messages"])[0]
            number=message["from"]
            text=message["text"]
            content=text["body"]
            texto="Registrar en EXP_BOL_MB" #cambiar por el valor de la variable text
            palabras = texto.split()
            cant_palabras=len(palabras)
            accion=palabras[0] #Aqui debe decir Registrar
            codLock=palabras[2] #aqui está el codigo del edificio
            if cant_palabras>=2 and accion=="Registrar":
                print("llegue /whatsapp")
                enviardirecto=whatsappservices.SendImageScren("https://static-files.aplus-security.com/787878_qr.jpg","59175002428")
                #utility=util.Registro(str(codLock),number)
                #imagenQR=qrconverter.CodeConverter('100003')
                return "EVENT_RECEIVED"
            
            elif accion!="Registrar":
                #utility2=util.VerifyNumber(number)
                return "EVENT_RECEIVED"
            #print(content)
            return "EVENT_RECEIVED"       
        except:
            return "EVENT_RECEIVED"  

#http://127.0.0.1:5000/movement/787879
@app.route('/movement/<codigo>',methods=['GET'])
#Aqui recibiré la notificación que hay un pedido por recoger y notificar al dpto
def ReceivedMov(codigo):
    print('llegue movimiento')
    code=codigo
    qrcode=qrconverter.CodeConverter(code)
    print(qrcode)
    url="https://static-files.aplus-security.com/"+qrcode+""
    print(url)
    move = actions.DbLockConn("SELECT * FROM movement WHERE code="+code+"")
   
    for fila in move:
        edificio=str(fila[3])
        dpto=str(fila[2])
        print(edificio)
        print(dpto)
        contacts=actions.DbLockConn("SELECT u.celular, u.name, b.name FROM user u INNER JOIN department d ON u.department_id=d.department_id INNER JOIN building b ON d.building_id=b.building_id WHERE u.department_id="+dpto+"")
        print(contacts)
        for contact in contacts:
            telefono=str(contact[0])
            print(telefono)
            envioqr=whatsappservices.SendImageScren(url,telefono)
    #sqlscript
    return "retorner movement"

def run():
    puerto = 8000
    print(f"Servidor arrancando en http://localhost:{puerto}")
    print("Usa la URL: http://localhost:8000/?archivo=nombrearchivo.ext")
    servidor = HTTPServer(('', puerto), MiHandler)
    servidor.serve_forever()

if(__name__=="__main__"):
   
    app.run(host='0.0.0.0', port=80)
    run()