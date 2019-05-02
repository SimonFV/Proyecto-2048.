#Proyecto Juego 2048
#Simon Fallas Villalobos

from tkinter import Tk
from tkinter import *
from tkinter import ttk, font
import random
import copy

class App():
    def __init__(self, master):


        self.r="sunken" #Bordes: "flat", "raised", "sunken", "ridge", "solid", "groove"
        self.c="gray40" #Color de las casillas de la matriz
        self.run=0   #Determina en que estado esta la interfaz, que se puede hacer y que no
        self.seg=1    #Segundos del cronometro
        self.min=5    #Segundos del cronometro
        self.puntos=0     #Puntuacion de la partida
        self.m=[0,1,2,3]   #Lista para la funcion que toma valores aleatorios
        self.x=[]       #Matriz principal del juego
        self.ve = master     #Ventana principal
        
        self.ve.geometry("520x460")
        self.ve.configure(bg = "gray40")
        self.ve.title("2048!!")

        #Frames donde se posicionan todos los widgets del juego
        self.gr = ttk.Frame(self.ve, padding=(5,5))   #Frame para la matriz
        self.gr2 = ttk.Frame(self.ve, padding=(5,5))   #Frame para el usuario
        self.gr3 = ttk.Frame(self.ve, padding=(5,5))    #Frame para la tabla
        self.gr4 = ttk.Frame(self.ve, padding=(5,5))    #Frame para la informacion y las opciones de base
        #Configuracion de los Frames
        self.gr.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
        self.gr2.grid(column=1, row=0, padx=5, pady=5, sticky=(N, S, E, W))
        self.gr3.grid(column=0, row=0, padx=5, pady=5, rowspan=2, sticky=(N, S, E, W))
        self.gr4.grid(column=0, row=2, padx=5, pady=5, columnspan=2, sticky=(N, S, E, W))

        #Labels de la puntuacion
        Label(self.gr4, text="Puntos: ").grid(pady=2, padx=2, row=0, column=2, sticky=(E))
        self.points = Label(self.gr4, text=self.puntos)
        self.points.grid(pady=2, padx=2, row=0, column=3, sticky=(W))
        #Labels del tiempo
        Label(self.gr4, text="TIEMPO: ").grid(pady=2, padx=2, row=0, column=4, sticky=(E))
        self.tiempo=Label(self.gr4, text="0:0")
        self.tiempo.grid(pady=2, padx=2, row=0, column=5, sticky=(W))
        #Label de informacion
        self.info=Label(self.gr4, text="INGRESE UN NOMBRE DE JUGADOR PARA INICIAR")
        self.info.grid(pady=2, padx=2, row=1, column=2, columnspan=4, sticky=(E))

        #Botones para escojer el modo de juego
        Button(self.gr4, text="BINARIO").grid(pady=2, padx=2, row=0, column=0, sticky=(E, W))
        Button(self.gr4, text="OCTAL").grid(pady=2, padx=2, row=1, column=0, sticky=(E, W))
        Button(self.gr4, text="DECIMAL").grid(pady=2, padx=2, row=0, column=1, sticky=(E, W))
        Button(self.gr4, text="HEXADECIMAL").grid(pady=2, padx=2, row=1, column=1, sticky=(E, W))

        #Labels de la tabla de puntuaciones
        score=open("Puntuaciones.txt", "r")
        self.sc=score.readlines()
        self.run=Label(self.gr3, text="RECORDS").grid(pady=2, padx=2, row=0, column=0, sticky=(N, S, E, W))
        self.tabla(1)
        score.close()

        #Labels de la matriz inicial
        self.ma00=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma00.grid(pady=4, padx=4, row=0, column=0, sticky=(N, S, E, W))
        self.ma01=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma01.grid(pady=4, padx=4, row=0, column=1, sticky=(N, S, E, W))
        self.ma02=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma02.grid(pady=4, padx=4, row=0, column=2, sticky=(N, S, E, W))
        self.ma03=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma03.grid(pady=4, padx=4, row=0, column=3, sticky=(N, S, E, W))
        self.ma10=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma10.grid(pady=4, padx=4, row=1, column=0, sticky=(N, S, E, W))
        self.ma11=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma11.grid(pady=4, padx=4, row=1, column=1, sticky=(N, S, E, W))
        self.ma12=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma12.grid(pady=4, padx=4, row=1, column=2, sticky=(N, S, E, W))
        self.ma13=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma13.grid(pady=4, padx=4, row=1, column=3, sticky=(N, S, E, W))
        self.ma20=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma20.grid(pady=4, padx=4, row=2, column=0, sticky=(N, S, E, W))
        self.ma21=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma21.grid(pady=4, padx=4, row=2, column=1, sticky=(N, S, E, W))
        self.ma22=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma22.grid(pady=4, padx=4, row=2, column=2, sticky=(N, S, E, W))
        self.ma23=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma23.grid(pady=4, padx=4, row=2, column=3, sticky=(N, S, E, W))
        self.ma30=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma30.grid(pady=4, padx=4, row=3, column=0, sticky=(N, S, E, W))
        self.ma31=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma31.grid(pady=4, padx=4, row=3, column=1, sticky=(N, S, E, W))
        self.ma32=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma32.grid(pady=4, padx=4, row=3, column=2, sticky=(N, S, E, W))
        self.ma33=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c)
        self.ma33.grid(pady=4, padx=4, row=3, column=3, sticky=(N, S, E, W))

        #Ingresar el usuario

        self.entry=Entry(self.gr2)
        self.entry.grid(row=0, column=1, sticky=(E, W))
        self.user()

        #Asignar el reajuste automatico a la ventana
        self.ve.columnconfigure(1, weight=1)
        self.ve.rowconfigure(1, weight=1)
        
        self.gr.columnconfigure(0, weight=1)
        self.gr.rowconfigure(0, weight=1)
        self.gr.columnconfigure(1, weight=1)
        self.gr.rowconfigure(1, weight=1)
        self.gr.columnconfigure(2, weight=1)
        self.gr.rowconfigure(2, weight=1)
        self.gr.columnconfigure(3, weight=1)
        self.gr.rowconfigure(3, weight=1)
        
        self.gr2.columnconfigure(0, weight=1)
        self.gr2.columnconfigure(1, weight=1)
        self.gr2.columnconfigure(2, weight=1)

        self.gr4.columnconfigure(2, weight=1)
        self.gr4.columnconfigure(3, weight=1)
        self.gr4.columnconfigure(4, weight=1)
        self.gr4.columnconfigure(5, weight=1)

        #Espera que se presione alguna flecha para realizar el movimiento
        self.ve.bind("<Up>", self.funcMove)
        self.ve.bind("<Down>", self.funcMove)
        self.ve.bind("<Left>", self.funcMove)
        self.ve.bind("<Right>", self.funcMove)

        
        self.ve.mainloop()
    
    #Metodo que construye los Labels de la matriz del juego
    def construir(self):
        self.forma(0,0)
        self.ma00.configure(text=self.x[0][0], relief=self.r, bg = self.c)
        self.forma(0,1)
        self.ma01.configure(text=self.x[0][1], relief=self.r, bg = self.c)
        self.forma(0,2)
        self.ma02.configure(text=self.x[0][2], relief=self.r, bg = self.c)
        self.forma(0,3)
        self.ma03.configure(text=self.x[0][3], relief=self.r, bg = self.c)
        self.forma(1,0)
        self.ma10.configure(text=self.x[1][0], relief=self.r, bg = self.c)
        self.forma(1,1)
        self.ma11.configure(text=self.x[1][1], relief=self.r, bg = self.c)
        self.forma(1,2)
        self.ma12.configure(text=self.x[1][2], relief=self.r, bg = self.c)
        self.forma(1,3)
        self.ma13.configure(text=self.x[1][3], relief=self.r, bg = self.c)
        self.forma(2,0)
        self.ma20.configure(text=self.x[2][0], relief=self.r, bg = self.c)
        self.forma(2,1)
        self.ma21.configure(text=self.x[2][1], relief=self.r, bg = self.c)
        self.forma(2,2)
        self.ma22.configure(text=self.x[2][2], relief=self.r, bg = self.c)
        self.forma(2,3)
        self.ma23.configure(text=self.x[2][3], relief=self.r, bg = self.c)
        self.forma(3,0)
        self.ma30.configure(text=self.x[3][0], relief=self.r, bg = self.c)
        self.forma(3,1)
        self.ma31.configure(text=self.x[3][1], relief=self.r, bg = self.c)
        self.forma(3,2)
        self.ma32.configure(text=self.x[3][2], relief=self.r, bg = self.c)
        self.forma(3,3)
        self.ma33.configure(text=self.x[3][3], relief=self.r, bg = self.c)
        

    #Da forma y color a las casillas de la matriz
    def forma(self,i,j):
        if(self.x[i][j]==0):
            self.r="sunken"
        else:
            self.r="raised"
        if(self.x[i][j]==0):   #colores: https://knowpapa.com/wp-content/uploads/2018/01/tkcolors.png
            self.c="gray40"
        elif(self.x[i][j]==2):
            self.c="lightskyblue1"
        elif(self.x[i][j]==4):
            self.c="skyblue1"
        elif(self.x[i][j]==8):
            self.c="deepskyblue"
        elif(self.x[i][j]==16):
            self.c="dodgerblue"
        elif(self.x[i][j]==32):
            self.c="cornflowerblue"
        elif(self.x[i][j]==64):
            self.c="blue"
        elif(self.x[i][j]==128):
            self.c="palegreen1"
        elif(self.x[i][j]==256):
            self.c="limegreen"
        elif(self.x[i][j]==512):
            self.c="greenyellow"
        elif(self.x[i][j]==1028):
            self.c="yellow"
        elif(self.x[i][j]==2048):
            self.c="magenta"
        elif(self.x[i][j]==4096):
            self.c="deeppink"
        else:
            self.c="reed"
        
            
    #Metodo que ejecuta la funcion indicada segun el movimiento recibido del teclado
    def funcMove(self,event):
        if(event.keysym=="Up"): 
            if(self.run==1):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,0,0,1,0,1,0,2,0,0,0))
        elif(event.keysym=="Down"):
            if(self.run==1):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,3,0,-1,0,1,0,1,0,0,0))
        elif(event.keysym=="Left"):
            if(self.run==1):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,0,0,0,1,0,1,2,1,0,0))
        elif(event.keysym=="Right"):
            if(self.run==1):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,0,3,0,-1,0,1,1,1,0,0))  
        self.x = d[0]
        self.puntos = self.puntos + d[1]
        p=copy.deepcopy(ran2(self.x))
        if(self.x!=z):
            if(p!=0):
                self.x[p[0]][p[1]]=ran([2,2,2,2,2,4])
                self.construir()
                self.points.configure(text=self.puntos)
            if(gameover(self.x,0,0,0)==False):
                self.run==0
                self.info.configure(text="PERDISTE: NO HAY MAS MOVIMIENTOS")
            
   

    #Metodo que crea la tabla de records
    def tabla(self,b):
        if(b<20):
            Label(self.gr3, text=self.sc[b][:-1]).grid(pady=2, padx=2, row=b, column=0, sticky=(N, S, E, W))
            Label(self.gr3, text=self.sc[b+1][:-1], bd=2, relief="ridge").grid(pady=2, padx=2, row=b, column=1, sticky=(N, S, E, W))
            self.tabla(b+2)

    #Metodo que guarda el usuario
    def user(self):
        Label(self.gr2, text="Usuario: ").grid(pady=5, padx=5, row=0, column=0, sticky=(E, W))
        self.entry.configure(state="normal")
        Button(self.gr2, command=self.user_play, text="Aceptar").grid(pady=2, padx=2, row=0, column=2, sticky=(E, W))
        
    #Metodo que guarda el usuario e inicia el juego
    def user_play(self):
        #Se crea la matriz con los valores aleatorios iniciales
        self.x=gam()
        #Construye los Labels de la matriz del juego
        self.construir()
        #Permite que se detecten las flechas
        self.run=1
        #Reccoje el nombre ingresado
        self.name=self.entry.get()
        self.cambiar_user()
        
        #Inicia el cronometro
        self.crono()
        
    #Metodo que permite cambiar el usuario
    def cambiar_user(self):
        Label(self.gr2, text="Usuario: ").grid(pady=5, padx=5, row=0, column=0, sticky=(E, W))
        self.entry.configure(state="readonly")
        Button(self.gr2, command=self.user, text="Cambiar").grid(pady=2, padx=2, row=0, column=2, sticky=(E, W))
        print(self.name)

    #Metodo que presenta el cronometro
    def crono(self):
        if(self.min>0):
            if(self.seg>0):
                self.seg=self.seg-1
                self.tiempo.configure(text=str(self.min)+":"+str(self.seg))
                self.tiempo.after(1000, self.crono)
            else:
                self.seg=59
                self.min=self.min-1
                self.tiempo.configure(text=str(self.min)+":"+str(self.seg))
                self.tiempo.after(1000, self.crono)
        
def gam():
    x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=[0,1,2,3]
    a=ran(m)
    b=ran(m)
    c=ran1(a,b,m)
    x[a][b]=ran([2,2,2,2,2,4])
    x[c[0]][c[1]]=ran([2,2,2,2,2,4])
    return x

#Escoje un valor aleatorio de una lista
def ran(m):
    y=random.choice(m)
    return y
#Escoje 2 casillas aleatorias para la matriz inicial 
def ran1(a,b,m):
    a2=ran(m)
    b2=ran(m)
    if(a==a2 and b==b2):
        return ran1(a,b,m)
    else:
        return [a2,b2]
#Escoje un valor aleatorio entre las casillas que quedan como 0

#x=[[0,2,0,0],[0,0,0,0],[0,4,0,0],[0,0,0,0]]
def ran2(x):
    c=[]
    c=zero(x,0,0,c)
    if(len(c)>0):
        d=ran(c)
        return [int(d[0]),int(d[1])]

    return 0
#Returna la lista de las casillas con ceros que quedan de la matriz
def zero(x,i,j,c):
    if(i<4):
        if(j<4):
            if(x[i][j]==0):
                c=c+[str(i)+str(j)]
                return zero(x,i,j+1,c)
            else:
                return zero(x,i,j+1,c)
        else:
            return zero(x,i+1,0,c)
    return c

#Funcion encargada de mover y sumar las casillas, y la puntuacion
#h=puntuacion
#Up: x, i=0, j=0, a=1, b=0, c=1, d=0, p=2, y=0, z=0
#Down: x, i=3, j=0, a=-1, b=0, c=1, d=0, p=1, y=0, z=0
#Left: x, i=0, j=0, a=0, b=1, c=0, d=1, p=2, y=1, z=0 
#Right: x, i=0, j=3, a=0, b=-1, c=0, d=1, p=1, y=1, z=0
def suma(x,i,j,a,b,c,d,p,y,z,h):
    if(3>=j and 3>=i):
        if(x[i][j]==0 and z!=2):
            x[i][j]=x[i+a][j+b]
            x[i+a][j+b]=0
            return suma(x,i+d,j+c,a,b,c,d,p,y,z,h)
        elif(x[i][j]==x[i+a][j+b] and z==2):
            h=h+x[i][j]+x[i][j]
            x[i][j]=x[i][j]+x[i][j]
            x[i+a][j+b]=0
            return suma(x,i+d,j+c,a,b,c,d,p,y,z,h)
        else:
            return suma(x,i+d,j+c,a,b,c,d,p,y,z,h)
    elif(y==0):
        if(p!=i):
            return suma(x,i+a,0,a,b,c,d,p,y,z,h)
        elif(z<3):
            if(p==2):
                return suma(x,0,0,a,b,c,d,p,y,z+1,h)
            else:
                return suma(x,3,0,a,b,c,d,p,y,z+1,h)
        else:
            return [x,h]
    else:
        if(p!=j):
            return suma(x,0,j+b,a,b,c,d,p,y,z,h)
        elif(z<3):
            if(p==2):
                return suma(x,0,0,a,b,c,d,p,y,z+1,h)
            else:
                return suma(x,0,3,a,b,c,d,p,y,z+1,h)
        else:
            return [x,h]
                
#Funcion que determina si todavia quedan movimientos
def gameover(x,i,j,z):
    if(z==0):
        if(i<3):
            if(x[i][j]==x[i+1][j] or x[i][j]==0):
                return True
            elif(x[i+1][j]==0):
                return True
            else:
                return gameover(x,i+1,j,z)
        elif(j<3):
            return gameover(x,0,j+1,z)
        else:
            return gameover(x,0,0,z+1)
    elif(z==1):
        if(j<3):
            if(x[i][j]==x[i][j+1] or x[i][j]==0):
                return True
            elif(x[i][j+1]==0):
                return True
            else:
                return gameover(x,i,j+1,z)
        elif(i<3):
            return gameover(x,i+1,0,z)
        else:
            return gameover(x,0,0,z+1)
    else:
        return False
        

def main():
    ve = Tk()
    game = App(ve)
    
    return 0

if __name__ == '__main__':
    main()

#Funcion que convierte de decimal a base binaria, octal o hexadecimal     
# x=int, b=base(2,8,16)
def dec_hex(x,b):
    if(x>b-1):
        if(x%b==10):
            return dec_hex(x//b,b) + "A"
        elif(x%b==11):
            return dec_hex(x//b,b) + "B"
        elif(x%b==12):
            return dec_hex(x//b,b) + "C"
        elif(x%b==13):
            return dec_hex(x//b,b) + "D"
        elif(x%b==14):
            return dec_hex(x//b,b) + "E"
        elif(x%b==15):
            return dec_hex(x//b,b) + "F"
        else:
            return dec_hex(x//b,b) + str(x%b)
    else:
        if(x%b==10):
            return "A"
        elif(x%b==11):
            return "B"
        elif(x%b==12):
            return "C"
        elif(x%b==13):
            return "D"
        elif(x%b==14):
            return "E"
        elif(x%b==15):
            return "F"
        else:
            return str(x%b)
        
