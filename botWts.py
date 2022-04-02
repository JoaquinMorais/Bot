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

def cleanMensage(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def elegirRespuesta(msg):
    mensage = str(msg).lower()
    mensage = cleanMensage(mensage)
    print(f"mensaje recibido: {mensage}")
    responses = ['Ehh Mesi','Aun no entiendo eso, pero con !help tal vez pueda ayudarte ;)','Simsimi un poroto','Veremos dijo el ciego','No puedo tengo fulbo','Perdon, no entiendo','La tuya por si acaso','No entendi pero habia una vez un choclo que iba andando en auto y choclo y murio xd','Uhhh no entendi, Estoy mas perdido q ciego en laberinto','Pao es gay','Sorry aun estoy en modo Mati y no soy capas de entender la poronga q me acabas de decir :(']
    if '!' == mensage[0]:
        if mensage == '!help':
            return "func01"
        elif mensage == '!hola':
            return "Hola!!! Soy un bot de prueba, escribiendo '!help' te daré una lista de comandos"
        elif mensage == '!turnoff':
            return "func02"

    if inList(mensage, ['hola','hi','hello','hey','buenas','buenos dias','buenas tardes','buenas noches']):
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
        responses = ['puto es tu hermano :D, trolo']
    elif 'contas un chiste' in mensage or 'decis un chiste' in mensage or 'conta un chiste' in mensage or 'contame un chiste' in mensage or 'contar un chiste' in mensage or 'haces un chiste' in mensage:
        responses = ['habia una vez un pollito q respiraba por el culito, se sento y se murio','habia una vez truz','En q se diferencia una feminista de un pokemon?\n Q los pokemones si evolucionan :D',
        'Sabes q te estas haciendo mayor cuando pasas por una iglesia y el cura no te guiña el ojo','Si un venezolano dice q sera pan comido, sera facil o dificil???','Si vas a comprar una leche siempre compra 1 o 2, Por q la tercera es la vencida :D',
        'Por q a un ladron lo entierran a 200 metros bajo tierra, por q en el fondo es bueno :D','Donde deja superman su capa? En su perchero :D','Sabes como le dicen a la hermana de Pao? Semaforo por q despues de las 12 nadie la respeta :D']    
    elif 'cantas una cancion' in mensage or 'cantas algo' in mensage or 'otra cancion' in mensage or 'sabes una cancion' in mensage or 'canta una cancion' in mensage or 'cantame' in mensage:
        responses = ['Vas a verme llegar\n Vas a oir mi cancion\n Vas a entrar sin pedirme la llaaaaaaveeeee\n La distancia del tiempo no sabe\n La falta q le haces\n A mi cooooraaaazoooooooooon',
        'Encontre al patito Juan\n Cuak Cuak Cuak\n En la esquina de San Juan\n Cuak Cuak Cuak', 'Paolooooo\n Le da Sabor a tu vida\n Paolo esta\n Desde el comienzo del diaaaaaaaa\n Mate cafe\n Harina y Palmitos...',
        'Fuisteee tu\n Tenerte fue una foto tuya puesta en mi cartera\n Un beso y verte hacer pequeño por la carretera\n Lo tuyo fue la intermitencia y la melancolia\n Lo mio fue aceptatlo todo por q te queria\n Verte llegar fue luz\n Verte partir un plus\n Fuiste Tuuuuuuu',
        'Dracukeo, el empalador\n La culeo, un taladrador\n Le meto el dedo, dice porfavo\n La caliento, soy un radiador\n Si no tiene los 18, eso es carcel\n Nonono\n Si no son mayores de edades\n Pa tucasa, a ver pocoyo']
    elif 'vs' in mensage or 'vos' in mensage:
        responses = ['bien bien aca ando','tan aburrido que voy a crear un bot para yo no poder trabajar mas :D, va a ser el bot del bot']
    
    
     
    return random.choice(responses)


def getMensage():
    pg.moveTo(ub)
    pg.tripleClick()
    pg.hotkey('ctrl','c')
    msg = clip.paste()
    pg.click()
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
        
        
        if boolean == False:
            
            respuesta = elegirRespuesta(getMensage())
            if 'func' in respuesta:
                if '01' in respuesta:
                    listado()
                elif '02' in respuesta:
                    break
            else:
                escribir(respuesta)
        
        if(aux==180):
            break
        time.sleep(1)

    escribir("Bot Apagado...")

def inList(mensage, lista):
    for i in lista:
        if i in mensage:
            return True
    return False



time.sleep(5)
prenderBot()