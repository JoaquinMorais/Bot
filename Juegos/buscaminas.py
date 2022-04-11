import random

class Buscaminas():
    def __init__(self):
        self.play = True
        self.ganas = False
        self.filas = 10
        self.columnas = 10
        self.minas = 10
        self.minasMarcadas = []
        self.visible = self.crearTablero('$')
        self.oculto= self.crearTablero(0)
        self.oculto,self.minasOcultas = self.generarMinas(self.oculto)

        self.y = random.randint(2,self.filas-3)
        self.x = random.randint(2,self.columnas-3)
        self.real = self.visible[self.y][self.x]
        self.visible[self.y][self.x] = "*E*"

        self.oculto = self.colocaPista(self.oculto)
        
        self.muestraTablero(self.visible)

    def iniciar(self):
        self.play = True
        self.ganas = False
        self.minasMarcadas = []
        self.visible = self.crearTablero('$')
        self.oculto= self.crearTablero(0)
        self.oculto,self.minasOcultas = self.generarMinas(self.oculto)
        self.y = random.randint(2,self.filas-3)
        self.x = random.randint(2,self.columnas-3)
        self.real = self.visible[self.y][self.x]
        self.visible[self.y][self.x] = "*E*"

        self.oculto = self.colocaPista(self.oculto)
        
        self.muestraTablero(self.visible)

    def crearTablero(self,valor):
        tablero = []
        for i in range(self.filas):
            tablero.append([])
            for j in range(self.columnas):
                tablero[i].append(valor)
        return tablero
    def muestraTablero(self,tablero):
        
        lista = []
        for fila in tablero:
            respuesta = ""
            for elem in fila:
                if str(elem) == "9":
                    elem = "*9*"
                respuesta += str(elem) + " "
            lista.append(respuesta)
        return lista
    
    def generarMinas(self,tablero):
        numero = 0
        minasOcultas = []
        while numero<self.minas:
            y = random.randint(0,self.filas-1)
            x = random.randint(0,self.columnas-1)
            if tablero[y][x] != '9':
                tablero[y][x] = '9'
                numero += 1
                minasOcultas.append([y,x])
        return tablero,minasOcultas
    
    def moverJugador(self):
        self.real = self.visible[self.y][self.x]
        self.visible[self.y][self.x] = "*E*"

    def jugando(self,mov):
        if mov == "w":
            if self.y == 0:
                self.y = 0
            else:
                self.visible[self.y][self.x] = self.real
                self.y -= 1
                self.moverJugador()
        elif mov == "s":
            if self.y == self.filas-1:
                self.y = self.filas-1
            else:
                self.visible[self.y][self.x] = self.real
                self.y += 1
                self.moverJugador()
        elif mov == "a":
            if self.x == 0:
                self.x = 0
            else:
                self.visible[self.y][self.x] = self.real
                self.x -= 1
                self.moverJugador()
        elif mov == "d":
            if self.x == self.columnas-1:
                self.x = self.columnas-1
            else:
                self.visible[self.y][self.x] = self.real
                self.x += 1
                self.moverJugador()
        elif mov == "b":
            if self.real == "$":
                self.visible[self.y][self.x] = "F"
                self.real = self.visible[self.y][self.x]
                if (self.y,self.x) not in self.minasMarcadas:
                    self.minasMarcadas.append((self.y,self.x))
        elif mov == "v":
            if self.real == "F":
                self.visible[self.y][self.x] = "$"
                self.real = self.visible[self.y][self.x]
                if (self.y,self.x) in self.minasMarcadas:
                    self.minasMarcadas.remove((self.y,self.x))

        elif mov == "m":
            if self.oculto[self.y][self.x] == "9":
                self.visible[self.y][self.x] = "*$*"
                self.play = False
            elif self.oculto[self.y][self.x] != 0:
                self.visible[self.y][self.x] = self.oculto[self.y][self.x]
                self.real = self.visible[self.y][self.x]
            elif self.oculto[self.y][self.x] == 0:
                self.visible[self.y][self.x] = 0
                self.visible = self.rellenado(self.oculto,self.visible)
                self.real = self.visible[self.y][self.x]
        
        if self.tableroCompleto() and sorted(self.minasOcultas) == sorted(self.minasMarcadas) and self.real != "$":
            self.ganas = True
            self.play = False


        return self.play,self.ganas
    def colocaPista(self,tablero):
        for y in range(self.filas):
            for x in range(self.columnas):
                if tablero[y][x] == "9":

                    for i in [-1, 0, 1]:

                        for j in [-1, 0, 1]:

                            if 0 <= y + i <= self.filas-1 and 0 <= x + j <= self.columnas-1:

                                if tablero[y+i][x+j] != "9":

                                    tablero[y+i][x+j] += 1
        
        return tablero
    def rellenado(self,oculto,visible):
        ceros = [(self.y,self.x)]
        while len(ceros) > 0:
            y,x = ceros.pop(0)
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if 0 <=y+1 <= self.filas-1 and 0 <= x+1 <= self.columnas-1:
                        if visible[y+i][x+j] == "$" and oculto[y+i][x+j] == 0 and oculto[y+i][x+j] == 0:
                            visible[y+i][x+j] = 0
                            if (y+i,x+j) not in ceros:
                                ceros.append((y+i,x+j))
                        else:
                            visible[y+i][x+j] = oculto[y+i][x+j]
        return visible
    def tableroCompleto(self):
        for y in range(self.filas):
            for x in range(self.columnas):
                if self.visible[y][x] == "$":
                    return False
        return True

    def getVisible(self):
        return self.visible
    def getOculto(self):
        return self.oculto