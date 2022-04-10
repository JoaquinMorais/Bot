import random

class Wordle():
    def __init__(self):
        self.palabras = ['perro','peses','diosa','obras','raspa','pesos','obras','nulos','nazis','nudos','matas','meras','manda','malos','jodes','hojas','hecho','haria','gasto','focos','frias','gafas','forro','lacra','jerga','japon','irian','india','iglus','gorra','giros','bondi','canas','campo','cajas','cacao','mujer','pelos','ramas','locos','coche','botas','botes','bruta']
        self.palabra = ""
        self.intento = 0

        self.resultados = ['-   -   -   -   -','-   -   -   -   -','-   -   -   -   -','-   -   -   -   -','-   -   -   -   -','-   -   -   -   -']
    
    def elegirPalabras(self):
        self.palabra=random.choice(self.palabras)
        print(self.palabra)
        self.resultados = ['-   -   -   -   -','-   -   -   -   -','-   -   -   -   -','-   -   -   -   -','-   -   -   -   -','-   -   -   -   -']
        self.intento = 0

    def comprobarPalabra(self,palabra):
        listBools = []
        
        for i in range(5):
            listBools.append(0)
            if palabra[i] in self.palabra:
                listBools[i] = 1
            
            if palabra[i] == self.palabra[i]:
                listBools[i] = 2
                
        resultado = ""
        for i in range(5):
            if listBools[i] == 0:
                resultado = f"{resultado} x "
            elif listBools[i] == 1:
                resultado = f"{resultado} _{palabra[i]}_ "
            elif listBools[i] == 2:
                resultado = f"{resultado} *{palabra[i]}* "
        

        self.resultados[self.intento] = resultado
        self.intento += 1
        return resultado
    
    def comprobarGanador(self,palabra):
        if self.palabra == palabra:
            return True
        else:
            return False
    def comprobarPerdedor(self):
        if self.intento == 6:
            return True
        else:
            return False
    
    def getResultados(self):
        return self.resultados
    def getPalabra(self):
        return self.palabra


