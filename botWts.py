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
    responses = ['Ehh Mesi','Aun no entiendo eso, pero con !help tal vez pueda ayudarte ;)','No puedo tengo fulbo','Perdon, no entiendo','La tuya por si acaso','No entendi pero habia una vez un choclo que iba andando en auto y choclo y murio xd','Uhhh no entendi, Estoy mas perdido q ciego en laberinto','Pao es gay','Sorry aun estoy en modo Mati y no soy capas de entender la poronga q me acabas de decir :(']
    if '!' in mensage:
        if mensage == '!help':
            return "func01"
        elif mensage == '!hola':
            return "Hola!!! Soy un bot de prueba, escribiendo '!help' te daré una lista de comandos"
        elif mensage == '!turnoff':
            return "func02"

    if 'hola' in mensage:
        responses = ['Holaa', 'Hola, que tal?', 'Hola, como estas?', 'Hola, que haces?','Tu nariz contra mis bolas']
    elif 'como estas' in mensage or 'como andas' in mensage or 'como te encontras' in mensage or 'todo bien?' in mensage or 'como te encontras' in mensage:
        responses = ['Muy bien, vs?', 'Muy bien, gracias por preguntar.', 'Todo piola vs??']
    elif 'q haces' in mensage or 'que haces' in mensage or 'nada vs' in mensage or 'nada vos' in mensage:
        responses = ['Aca tranqui, Vs?', 'Molestando a Gucci vs?', 'Aca Hablando con un boludo :D\n Nooo estaba re enojado el bot']
    elif 'cuantos años tenes' in mensage or 'cual es tu edad' in mensage:
        responses = ['Recien Naci', 'Hace un par de horas', 'Un Milenio']
    elif 'jajaj' in mensage:
        responses = ['Jajajajaj', 'Jajsjsaj', 'Q te reis gay']
    elif 'tu tia' in mensage or 'tu prima' in mensage:
        responses = ['la tuya con sandia']
    elif 'tu hermana' in mensage:
        responses = ['la tuya con banana']
    elif 'xd' in mensage:
        responses = ['xd']
    elif 'puto' in mensage:
        responses = ['puto es tu hermano :D']

    elif 'vs' in mensage or 'vos' in mensage:
        responses = ['bien bien aca ando','tan aburrido que voy a crear un bot para yo no poder trabajar mas :D, va a ser el bot del bot']
    
    
     
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
        
        if(aux==200):
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