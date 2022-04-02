from http.client import responses
import pyautogui as pg
import time
import random, re
import pyperclip as clip



ub = 700,932
barra = 700,1004

"""
time.sleep(2)


try:
    new_msg = pg.locateOnScreen('msg.png',confidence=.1)

    if new_msg is not None:
        pg.moveTo(new_msg)
        pg.moveRel(-150,0)
        pg.click()
        time.sleep(.5)
        print("New message detected")
    else:
        print("No new message detected")
except:
    print("Error")
    pass
"""

def cleanMensage(msg):
    vocals = ['a','e','i','o','u']
    for index, item in enumerate(['á','é','í','ó','ú']):
        if item in msg:
            clean_txt = msg.replace(item,vocals[index])
        else:
            clean_txt = msg
    return clean_txt

def elegirRespuesta(msg):
    mensage = str(msg).lower()
    mensage = cleanMensage(mensage)
    responses = ['Ehh Mesi']
    if '!' in mensage:
        if mensage == '!help':
            return "func01"
        elif mensage == '!hola':
            return "Hola!!! Soy un bot de prueba, escribiendo '!help' te daré una lista de comandos"
        elif mensage == '!turnoff':
            return "func02"

    if 'hola' in mensage:
        responses = ['Hola', 'Hola, que tal', 'Hola, como estas', 'Hola, como estas?','Tu nariz contra mis bolas']
    elif 'vs' in mensage or 'vos' in mensage or 'como estas' in mensage or 'como andas' in mensage or 'como te encontras' in mensage or 'todo bien' in mensage or 'como te encontras' in mensage:
        responses = ['Muy bien', 'Muy bien, gracias por preguntar.', 'Muy piola']
    elif 'q haces' in mensage or 'que haces' in mensage:
        responses = ['Aca piola, Vs?', 'Molestando a Gucci vs?', 'Aca Hablando con un boludo :D\n Nooo estaba re enojado el bot']
    elif 'cuantos años tenes' in mensage or 'cual es tu edad' in mensage:
        responses = ['Recien Naci', 'Hace un par de horas', 'Un Milenio']
    
     
    return random.choice(responses)


def getMensage():
    pg.moveTo(ub)
    pg.tripleClick()
    pg.hotkey('ctrl','c')
    msg = clip.paste()
    pg.click()
    print(f"mensaje recibido: {msg}")
    return msg





def escribir(texto):
    pg.moveTo(barra)
    pg.doubleClick()
    pg.typewrite(f"{texto}\n")

def listado():
    pg.moveTo(barra)
    pg.doubleClick()
    pg.typewrite(f"Listado de comandos:")
    pg.hotkey('shift','enter')
    pg.typewrite(f"!help: Ayuda")
    pg.hotkey('shift','enter')
    pg.typewrite(f"!hola: Saludo")
    pg.hotkey('shift','enter')
    pg.typewrite(f"!turnoff: Apagar El Bot")
    pg.hotkey('shift','enter')
    pg.typewrite(f"\n")





def prenderBot():
    aux = 0
    escribir("Bot Encendido")
    while True:
        aux+=1
        boolean = pg.pixelMatchesColor(ub[0],ub[1],(17,25,31))
        print(boolean)
        
        if boolean == False:
            print("Nuevo Mensaje")
            respuesta = elegirRespuesta(getMensage())
            if 'func' in respuesta:
                if '01' in respuesta:
                    listado()
                elif '02' in respuesta:
                    break
            else:
                escribir(respuesta)
        
        if(aux==30):
            break
        time.sleep(1)

    escribir("Bot Apagado...")

def pruebaTexto(mensage):
    if 'hola' in mensage:
        return True
    else:
        return False



time.sleep(5)
prenderBot()