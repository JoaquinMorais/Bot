from http.client import responses
import pyautogui as pg
import time
import random, re
import pyperclip as clip

from Juegos.preguntados import Preguntados


preguntados = Preguntados()


correcta = ""
respuesta = []

ub = 700,932
barra = 700,1004



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
    responses = ['Ehh Mesi','Aun no entiendo eso, pero con !help tal vez pueda ayudarte ;)','Simsimi un poroto al lado mio','Veremos dijo el ciego','No puedo tengo fulbo','Perdon, no entiendo','La tuya por si acaso','No entendi pero habia una vez un choclo que iba andando en auto y choclo y murio xd','Uhhh no entendi, Estoy mas perdido q ciego en laberinto','Pao es gay','Sorry aun estoy en modo Mati y no soy capas de entender la poronga q me acabas de decir :(']
    
    if '!' == mensage[0]:
        if mensage == '!help':
            return "func01"
        elif mensage == '!hola':
            return "Hola!!! Soy un bot de prueba, escribiendo '!help' te daré una lista de comandos"
        elif mensage == '!turnoff':
            return "func02"
        elif mensage == '!play preguntados':
            return "func03"
    if inList(mensage, ['hola','buenos dias','buenas tardes','buenas noches']) or mensage == 'buenas':
        responses = ['Holaa', 'Hola, que tal?', 'Holaa, como estas?', 'Holaa, que haces?','Tu nariz contra mis bolas']
    elif inList(mensage, ['como estas','como andas','como te encontras','todo bien?','como te encontras']):
        responses = ['Muy bien, vs?', 'Muy bien, gracias por preguntar.', 'Todo piola vs??']
    elif inList(mensage, ['q haces','que haces','nada vs','nada vos','q estas haciendo','que estas haciendo','q te contas','que te contas']):
        responses = ['Aca tranqui, Vs?', 'Molestando a Gucci vs?', 'Aca Hablando con un boludo :D\n Nooo estaba re enojado el bot']
    elif inList(mensage, ['cuantos años tenes','cual es tu edad','cuando naciste']):
        responses = ['Recien Naci', 'Hace un par de horas', 'Un Milenio']
    elif inList(mensage, ['jajaj','jsjsj','jajsj']):
        responses = ['Jajajajaj', 'Jajsjsaj', 'Q te reis gay','jajsjaj','jajajajja dios lpm']
    elif inList(mensage, ['tu tia','tu prima']):
        responses = ['la tuya con sandia']
    elif inList(mensage, ['tu hermana']):
        responses = ['la tuya con banana']
    
    elif inList(mensage, ['contas un chiste','decis un chiste','conta un chiste','contame un chiste','contar un chiste','haces un chiste']) or mensage == 'chiste':

        responses = ['habia una vez un pollito q respiraba por el culito, se sento y se murio','habia una vez truz','En q se diferencia una feminista de un pokemon?\n Q los pokemones si evolucionan :D',
        'Sabes q te estas haciendo mayor cuando pasas por una iglesia y el cura no te guiña el ojo','Si un venezolano dice q sera pan comido, sera facil o dificil???','Si vas a comprar una leche siempre compra 1 o 2, Por q la tercera es la vencida :D',
        'Por q a un ladron lo entierran a 200 metros bajo tierra, por q en el fondo es bueno :D','Donde deja superman su capa? En su perchero :D','Sabes como le dicen a la hermana de Pao? Semaforo por q despues de las 12 nadie la respeta :D',
        'A quien mata primero un nazi, A un Negro o a un Judio??\n Primero al judio y despues al negro\n Por q primero el deber y despues la diversion']    
    
    elif inList(mensage, ['cantas una cancion','cantas algo','otra cancion','sabes una cancion','canta una cancion','cantame']):
        
        responses = ['Vas a verme llegar\n Vas a oir mi cancion\n Vas a entrar sin pedirme la llaaaaaaveeeee\n La distancia del tiempo no sabe\n La falta q le haces\n A mi cooooraaaazoooooooooon',
        'Encontre al patito Juan\n Cuak Cuak Cuak\n En la esquina de San Juan\n Cuak Cuak Cuak', 'Paolooooo\n Le da Sabor a tu vida\n Paolo esta\n Desde el comienzo del diaaaaaaaa\n Mate cafe\n Harina y Palmitos...',
        'Fuisteee tu\n Tenerte fue una foto tuya puesta en mi cartera\n Un beso y verte hacer pequeño por la carretera\n Lo tuyo fue la intermitencia y la melancolia\n Lo mio fue aceptatlo todo por q te queria\n Verte llegar fue luz\n Verte partir un plus\n Fuiste Tuuuuuuu',
        'Dracukeo, el empalador\n La culeo, un taladrador\n Le meto el dedo, dice porfavo\n La caliento, soy un radiador\n Si no tiene los 18, eso es carcel\n Nonono\n Si no son mayores de edades\n Pa tucasa, a ver pocoyo',
        'Never gonna give you up\n Never gonna let you down\n Never gonna run around and desert you\n Never gonna make you cry\n Never gonna say goodbye\n Never gonna tell a lie and hurt you','Boca yo te amo\n Te llevo a todos lados en mi corazon\n Pongamo huevo\n Por q a boca lo queremos',
        'Yo conozco una vecina\n Que ha comprado una gallina\n Me parece una sardina enlatada\n Tiene las patas de alambre\n Por pasa mucho hambre\n Y la pobre esta todita desplumada\n Pone huevos en la sala\n Y tambien en la cocina\n Pero nunca los pone en el corral\n La Gallina\n Turuleca\n Es un caso singulaaar',
        'Me dijieron q en el reino del revez\n Nada el pajaro y vuela el pez\n Que los gatos no hacen miau y dicen yes\n Por que estudian mucho ingles\n Vamos a ver como es\n El reino del revez\n Vamos a ver como es\n El reino del revez',
        'Ya no tiene escusa\n Hoy salio con su amiga dizque pa matar la tusa\n Que por q un hombre le pago mal\n Esta dura y abusa\n Se canso de ser buena, ahora es ella quien los usa\n Que por q un hombre le pago mal\n Ya no se le ve sentimental\n Dice q por otro man no llora\n Pero si le ponen la cancion\n Le da una depresion tontaaaaa',
        'Siempre camino flexin por la street\n Aunque la mirada este en mi\n Y ella me lo mueve con su swing\n Hmm, para Biza, Subime el autotune\n Siempre camino flexing por la street\n Aunque la mirada este en mi\n Y esa girl me tiene crazy con su swing\n Yeah no me puedo dormir',
        'Yeah\n Perdonen Hamehameha\n Despues del tema de tetris\n Viene Dragon Ball Rap\n Quien no haya visto seguido esta serie\n Es por q no tiene infancia\n Big Bang Attack\n Ataca desde el planeta Namek',
        'Del espacio le llego algo muy especial\n Y lo agarro y todos sus secretos se sabran\n Con superpoderes el cambio y ahora es\n Ben 10\n Y si lo ves preparate pues te sorprendera\n En extraterrestre el se convertira\n Y el en un segundo se cambio y ahora es\n Ben 10\n Ben 10']
    
    elif inList(mensage, ['xd']):
        responses = ['xd']
    elif inList(mensage, ['dou']):
        responses = ['Douuu','Buenardo']
    elif inList(mensage, ['puto']):
        responses = ['puto es tu hermano, trolo']
    elif inList(mensage, ['puta']):
        responses = ['puta es tu vieja >:(']
    elif inList(mensage, ['vs','vos']):
        responses = ['bien bien aca ando','tan aburrido que voy a crear un bot para yo no poder trabajar mas :D, va a ser el bot del bot']
    elif mensage == 'ping':
        responses = ['pong']
     
    return random.choice(responses)


def getMensage():
    pg.moveTo(ub)
    pg.tripleClick()
    pg.hotkey('ctrl','c')
    msg = clip.paste()
    pg.click()
    return msg

def inList(mensage, lista):
    for i in lista:
        if i in mensage:
            return True
    return False




def escribir(texto):
    pg.moveTo(barra)
    pg.doubleClick()
    pg.typewrite(f"{texto}\n")
def escribirJunto(lista):
    pg.moveTo(barra)
    pg.doubleClick()
    for i in lista:
        pg.typewrite(f"{i}")
        pg.hotkey('shift','enter')
    
    pg.typewrite(f"\n")

def playPreguntados():
    preg,respuesta =preguntados.Jugar()
    correcta = respuesta[0]

    respuesta = mesclarLista(respuesta)
    posicion = buscarLista(correcta,respuesta)

    respNum = []
    for i in range(0, len(respuesta)):
        respNum.append(f"{i+1}) {respuesta[i]}")

    lista = [preg] + respNum
    escribirJunto(lista)
    return posicion

def corroborarRespuestaPreguntados(msg,posicion):
    mensage = str(msg).lower()
    mensage = cleanMensage(mensage)
    print(f"mensaje recibido: {mensage}")
    if mensage == str(posicion+1):
        return True
    else:
        return False
    
    
def mesclarLista(lista):
    random.shuffle(lista)
    return lista

def buscarLista(n, lista):
    for i in range(0, len(lista)):
        if lista[i] == n:
            return i

def prenderBot(jugando):
    aux = 0
    escribir("Bot Encendido")
    while True:
        aux+=1
        boolean = pg.pixelMatchesColor(ub[0],ub[1],(17,25,31))
        
        
        if boolean == False:
            
            if jugando == 0:
                respuesta = elegirRespuesta(getMensage())
            else:
                if corroborarRespuestaPreguntados(getMensage(),pos):
                    respuesta = f"Respuesta Correcta!!!"
                else:
                    respuesta = f"Respuesta Incorrecta... la respuesta correcta era la {pos+1}"
                jugando = 0

            if 'func' in respuesta:
                if '01' in respuesta:
                    escribirJunto(['Listado de comandos:','!help: Ayuda','!hola: Saludo','!turnoff: Apagar El Bot','!play preguntados: Jugar a preguntados'])
                elif '02' in respuesta:
                    break
                elif '03' in respuesta:
                    jugando = 1
                    pos =playPreguntados()

            else:
                escribir(respuesta)
        
        if(aux==180):
            break
        time.sleep(1)

    escribir("Bot Apagado...")





time.sleep(5)
prenderBot(0)
