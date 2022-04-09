import random


class Ahorcado:
    def __init__(self):
        self.palabras = ['casa','perro','gato','coche','planta','ahorcado','mujer','hombre']
        self.palabra = ""
        self.palabraOculta = ""
        self.letras = []
        self.fallos = 0
                
    
    def mostrarTablero(self,n):
        if n == 1:
            return "foto1"
        elif n == 2:
            return "foto2"
        elif n == 3:
            return "foto3"
        elif n == 4:
            return "foto4"
        elif n == 5:
            return "foto5"
        elif n == 6:
            return "foto6"
        elif n == 7:
            return "foto7"
        
    def mostrarPalabra(self,palabra):
        for i in palabra:
            pass
    
    def elegirPalabra(self):
        self.palabra = random.choice(self.palabras)
        self.palabraOculta = len(self.palabra) * "-"

        return self.palabra,self.palabraOculta

    def comprobarLetra(self,letra):
        boolean  = False
        
        if letra in self.palabra:
            for i in range(len(self.palabra)):
                if self.palabra[i] == letra:
                    self.palabraOculta = self.palabraOculta[:i] + letra + self.palabraOculta[i+1:]
                    boolean = True
        else:
            self.fallos += 1
            print("Fallo")

        
        print(self.palabra)
        print(self.palabraOculta)

        return boolean, self.palabraOculta, self.fallos
    
    def comprobarGanador(self):
        if self.palabra == self.palabraOculta:
            return True
        else:
            return False
    
    def comprobarPerdedor(self):
        if self.fallos == 6:
            return True
        else:
            return False
    def getPalabra(self):
        return self.palabra

