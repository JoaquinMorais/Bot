import click
import pyautogui as pg
import time
import random

tiempo = 0.001
cantidad = 5
numTelefono = "" #Ejemplo: +56912345678
texto = "Hola"


barraDeWts = 700,1004 #(x,y), depende el monitor, si no funciona, cambiarlo

def abrir(pos,click=1):
    pg.moveTo(pos)
    pg.click(clicks=click)


def Main(n):
    Hacker()
    time.sleep(5)
    Inicio()
    BraveRick(1)
    CosasRandom(n)

def Exploradores():
    Inicio()
    ExploradorDeArchivos()
    NavegadorChorme()
    NavegadorOpera()
    NavegadorBrave()
    NavegadorFirefox()
def Hacker():
    pg.hotkey('win','r')
    pg.typewrite('cmd\n',0.1)
    pg.typewrite('color a\n',0.01)
    pg.typewrite('tree\n',0.01)
    pg.typewrite('tree\n',0.01)
    pg.hotkey('win','t')
    
    

def Inicio():
    pg.hotkey('win', 'r')
    pg.typewrite('notepad\n')
    pg.typewrite('Ahora tienes un virus :)\n',0.1)
    time.sleep(1)
def ExploradorDeArchivos():
    pg.hotkey('win','e')
    pg.hotkey('win','t')
    time.sleep(0.1)

def NavegadorChorme():
    pg.hotkey('win','r')
    pg.typewrite('chrome\n',tiempo)
    pg.hotkey('win','t')

def NavegadorFirefox():
    pg.hotkey('win','r')
    pg.typewrite('firefox\n',tiempo)
    pg.hotkey('win','t')


def NavegadorOpera():
    pg.hotkey('win','r')
    pg.typewrite('opera\n',tiempo)
    pg.hotkey('win','t')


def NavegadorBrave():
    pg.hotkey('win','r')
    pg.typewrite('brave\n',tiempo)
    pg.hotkey('win','t')

def CosasRandom(n):
    for i in range(0,n):
        numero = random.randint(1,5)
        if numero == 1:
            NavegadorBrave()
        if numero == 2:
            NavegadorChorme()
        if numero == 3:
            NavegadorFirefox()
        if numero == 4:
            NavegadorOpera()
        if numero == 5:
            ExploradorDeArchivos()

def BraveRick(n):
    for i in range(0,n):
        pg.hotkey('win','r')
        pg.typewrite('brave\n',tiempo)
        pg.typewrite("https://youtu.be/mCdA4bJAGGk\n",0.01)


def MuchosExploradores(n):
    for i in range(0,n):
        ExploradorDeArchivos()
        

def WhatsApp(n):
    pg.hotkey('win','r')
    pg.typewrite('brave\n',tiempo)
    pg.typewrite(f"https://web.whatsapp.com/send?phone=+{numTelefono}\n",0.001)
    time.sleep(10)
    abrir(barraDeWts)
    abrir(barraDeWts)
    
    for i in range(0,n):
        pg.typewrite(f"{texto}\n")

def Alerta(t1,t2):
    pg.alert("BOENAAAS")
    
def clicks(n):
    time.sleep(10)

    for i in range(0,n):
        pg.click(clicks=1)






print(pg.displayMousePosition())