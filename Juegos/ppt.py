#Piedra Papel o Tijeras
import random


class PPT():
    def __init__(self):
        self.opciones = ["piedra", "papel", "tijeras"]
        self.opcion = ""
        self.iniciando()
        
    def iniciando(self):
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0

    def elegirOpcion(self):
        self.opcion = random.choice(self.opciones)
    def comprobarPalabra(self,palabra):
        if palabra in self.opciones:
            return True
        else:
            return False

    
    def jugar(self,palabra):
        self.elegirOpcion()
        if palabra == "tijeras":
            if self.opcion == "papel":
                return 0
            elif self.opcion == "piedra":
                return 1
            elif self.opcion == "tijeras":
                return 2
        elif palabra == "piedra":
            if self.opcion == "papel":
                return 1
            elif self.opcion == "piedra":
                return 2
            elif self.opcion == "tijeras":
                return 0
        elif palabra == "papel":
            if self.opcion == "papel":
                return 2
            elif self.opcion == "piedra":
                return 0
            elif self.opcion == "tijeras":
                return 1

    def resultado(self,mensaje):
        if mensaje == 0:
            self.victorias += 1
            return random.choice("Ganaste -.-",'Te la doy como buena...','Ahhhh','Puto','-.-')
        elif mensaje == 1:
            self.derrotas += 1
            return random.choice("Te gane, a casa malo",'A casa Pete,','Pal lobbyyyy','A tomar la leche')
        elif mensaje == 2:
            self.empates += 1
            return "Empate :("
    def getVictorias(self):
        return self.victorias
    def getDerrotas(self):
        return self.derrotas
    def getEmpates(self):
        return self.empates
    def getResultado(self):
        return self.opcion
ppt = PPT()
