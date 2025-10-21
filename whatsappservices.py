import requests
import json
tk="8DA64BEAD41A-4C41-B565-4BD1C72915AF"#"FB2C96A5256D-4431-96E8-E0E3C971892D"##"EAAWye57tM5IBPhY6gtlcYYoZBUA5MEE1ZAw8XMRfMZC4QmnZBBDfwpsvHyBAZAS3a1d3m3yDdwOIu5eF4cBNH2fzMxuBb8hdqhyz34eWKZAHHYOnpSzIvy85FL4n2IiUdkktVB7ZCZCs1ZA17Ohq2PbDpNcm2zs8zN1ao5B7KhRAPv110Jo8MZCvHLkZA5BoqZB6J3VHhCcC4eIsLtkOVtoiCkiCYKoJVCd0UlR39M5S"
lk="https://evo-api-evolution-api.g8y8m7.easypanel.host/message/sendMedia/locker"#"https://evolutionapi-evolution-api.9wmqx3.easypanel.host/message/sendMedia/testsergio"#"https://graph.facebook.com/v22.0/870846042775736/messages "
def SendMessageWhatsapp(textUser, number):
    try:
        print(textUser,number) 
        token=tk
        api_url=lk
        print(api_url)
        data={
               "messaging_product": "whatsapp", "to": "59175002428", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } }  
            }
        print(data)
        headers={"apikey": token,"Content-Type": "application/json"}
        response=requests.post(api_url, data=json.dumps(data), headers=headers)
        print(response.json())
        if response.status_code==200:
            return True
        return False
    except  Exception as exception:
        print("exception "+exception)
        return False

def SendImagewhatsapp(number,image):
    print( "llegue SendImageWhatsApp")
    print("URL: " + image)
    try:
        token=tk
        api_url=lk
        data={
               "messaging_product": "whatsapp", "to": '59167744007', "type": "image", "image": { "link": "https://images.pexels.com/photos/159304/network-cable-ethernet-computer-159304.jpeg"}  
            }
        headers={"apikey": +token,"Content-Type": "application/json"}
        response=requests.post(api_url, data=json.dumps(data), headers=headers)
        print(response.json())
        if response.status_code==200:
            return True
        return False
    except  Exception as exception:
        print("exception "+exception)
        return False
    
def SendImageScren(link, telefono):
        print("Llegue SendImageScren")
        print(link)
        print(telefono)
        try: 
            url = lk
            access_token = tk
            url2=link
            headers = {
                "apikey": access_token,
                "Content-Type": "application/json"
            }
            payload = {
                            
                    "number": "59175679775",
                    "mediatype": "image", # image, video or document
                    "mimetype": "image/jpeg",
                    "caption": "Test de QR",
                    "media": "https://images.pexels.com/photos/159304/network-cable-ethernet-computer-159304.jpeg", #/* url or base64 */
                    "fileName": "68a384c439c70.png"

                
            }
            response = requests.post(url, json=payload, headers=headers)
            print("RESPONSEE")
            print(response.json())
            print("Saliendo RESPONSE0000")
            print(response.status_code)
            if response.status_code==200:
                return True
            return False
        except Exception as exception:
            print("EXCEPTIOOON")
            print("exeption :" )
            print("Saliendo exception")
            return False
def SearchNumberOnBD(number):
    #Aqui me conecto a la BD y en la Tabla xx buscaré si el numero de origen ya existe y devuelvo un True o False
    return
