from flask import Flask, request, send_from_directory
import qrconverter
import whatsappservices
import util
import actions


app=Flask(__name__)


@app.route('/welcome/<name>',methods=['GET'])
def index(name):  
    ver_files=util.VerFiles(name)
  
    
    return "Bienvenido a WABA_Bot for Holding Home4"+ver_files

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

if(__name__=="__main__"):
   
    app.run(host='0.0.0.0', port=80)