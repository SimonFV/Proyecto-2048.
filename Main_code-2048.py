#Proyecto Juego 2048
#Simon Fallas Villalobos

from tkinter import Tk
from tkinter import *
from tkinter import ttk, font
import random
import copy
#Borders: "flat", "raised", "sunken", "ridge", "solid", "groove"

#Clase que crea la ventana completa del juego.
class App():
    def __init__(self, master, x):

        self.puntos=0
        self.m=[0,1,2,3]
        self.x=x
        self.ve = master
        self.ve.geometry("520x460")
        self.ve.configure(bg = "gray40")
        self.ve.title("2048!!")
        
        self.gr = ttk.Frame(self.ve, padding=(5,5))
        self.gr2 = ttk.Frame(self.ve, padding=(5,5))
        self.gr3 = ttk.Frame(self.ve, padding=(5,5))
        self.gr4 = ttk.Frame(self.ve, padding=(5,5))

        self.gr2.grid(column=1, row=0, padx=5, pady=5, sticky=(N, S, E, W))
        self.gr.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
        self.gr3.grid(column=0, row=0, padx=5, pady=5, rowspan=2, sticky=(N, S, E, W))
        self.gr4.grid(column=0, row=2, padx=5, pady=5, columnspan=2, sticky=(N, S, E, W))

        self.info=Label(self.gr4, text="Ingrese usuario para iniciar.").grid(pady=2, padx=2, row=1, column=3, sticky=(E))
        self.mode1=Button(self.gr4, text="Suma").grid(pady=2, padx=2, row=0, column=0, sticky=(E, W))
        self.mode2=Button(self.gr4, text="Multp").grid(pady=2, padx=2, row=1, column=0, sticky=(E, W))
        self.base10=Button(self.gr4, text="Dec").grid(pady=2, padx=2, row=0, column=1, sticky=(E, W))
        self.binario=Button(self.gr4, text="Bin").grid(pady=2, padx=2, row=1, column=1, sticky=(E, W))
        self.octal=Button(self.gr4, text="Oct").grid(pady=2, padx=2, row=0, column=2, sticky=(E, W))
        self.hexa=Button(self.gr4, text="Hex").grid(pady=2, padx=2, row=1, column=2, sticky=(E, W))
        #Labels de la tabla de puntuaciones
        self.ta=Label(self.gr3, text="Records", bd=2, relief="ridge").grid(pady=2, padx=2, row=0, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user1: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=1, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user2: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=2, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user3: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=3, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user4: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=4, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user5: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=5, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user6: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=6, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user7: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=7, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user8: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=8, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user9: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=9, column=0, sticky=(N, S, E, W))
        self.ta=Label(self.gr3, text="user10: 000", bd=2, relief="ridge").grid(pady=2, padx=2, row=10, column=0, sticky=(N, S, E, W))
        #Ingresar el usuario
        self.user=Label(self.gr2, text="User: ").grid(pady=5, padx=5, row=0, column=0, sticky=(E, W))
        self.name=Entry(self.gr2).grid(row=0, column=1, sticky=(E, W))
        self.at=Button(self.gr2, text="Aceptar").grid(pady=2, padx=2, row=0, column=2, sticky=(E, W))

        #Metodo que construye los Labels de la matriz del juego
        self.construir(0,0)
        
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

        self.gr4.columnconfigure(3, weight=1)

        #Espera que se presione alguna flecha para llamar al metodo indicado
        self.ve.bind("<Up>", self.funcUp)
        self.ve.bind("<Down>", self.funcDown)
        self.ve.bind("<Left>", self.funcLeft)
        self.ve.bind("<Right>", self.funcRight)


        self.ve.mainloop()
        
    #Metodo que construye los Labels de la matriz del juego
    def construir(self,i,j):
        if(i<4):
            if(j<4):
                if(self.x[i][j]==0):
                    r="sunken"
                else:
                    r="raised"
                if(self.x[i][j]==0):   #colores: https://knowpapa.com/wp-content/uploads/2018/01/tkcolors.png
                    c="gray40"
                elif(self.x[i][j]==2):
                    c="lightskyblue1"
                elif(self.x[i][j]==4):
                    c="skyblue1"
                elif(self.x[i][j]==8):
                    c="deepskyblue"
                elif(self.x[i][j]==16):
                    c="dodgerblue"
                elif(self.x[i][j]==32):
                    c="cornflowerblue"
                elif(self.x[i][j]==64):
                    c="blue"
                elif(self.x[i][j]==128):
                    c="palegreen1"
                Label(self.gr, text=self.x[i][j], bd=1, relief=r, bg = c).grid(pady=4, padx=4, row=i, column=j, sticky=(N, S, E, W))
                self.construir(i, j+1)
            else:
                self.construir(i+1,0)
            

    #Metodos que cambian los valores de la matriz
    def funcUp(self,_event=None):
        z=copy.deepcopy(self.x)
        d = copy.deepcopy(suma(self.x,0,0,1,0,1,0,2,0,0,0))
        self.x = d[0]
        self.puntos = self.puntos + d[1] 
        p=copy.deepcopy(ran2(self.x,self.m,0,0))
        if(self.x!=z):
            self.x[p[0]][p[1]]=ran([2,2,2,2,4])
            self.construir(0,0)
            print(self.puntos)
    def funcDown(self,_event=None):
        z=copy.deepcopy(self.x)
        d = copy.deepcopy(suma(self.x,3,0,-1,0,1,0,1,0,0,0))
        self.x = d[0]
        self.puntos = self.puntos + d[1] 
        p=copy.deepcopy(ran2(self.x,self.m,0,0))
        if(self.x!=z):
            self.x[p[0]][p[1]]=ran([2,2,2,2,4])
            self.construir(0,0)
            print(self.puntos)
    def funcLeft(self,_event=None):
        z=copy.deepcopy(self.x)
        d = copy.deepcopy(suma(self.x,0,0,0,1,0,1,2,1,0,0))
        self.x = d[0]
        self.puntos = self.puntos + d[1] 
        p=copy.deepcopy(ran2(self.x,self.m,0,0))
        if(self.x!=z):
            self.x[p[0]][p[1]]=ran([2,2,2,2,4])
            self.construir(0,0)
            print(self.puntos)
    def funcRight(self,_event=None):
        z=copy.deepcopy(self.x)
        d = copy.deepcopy(suma(self.x,0,3,0,-1,0,1,1,1,0,0))
        self.x = d[0]
        self.puntos = self.puntos + d[1] 
        p=copy.deepcopy(ran2(self.x,self.m,0,0))
        if(self.x!=z):
            self.x[p[0]][p[1]]=ran([2,2,2,2,4])
            self.construir(0,0)
            print(self.puntos)

#Funcion que define la matriz inicial del juego
def gam():
    x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=[0,1,2,3]
    a=ran(m)
    b=ran(m)
    c=ran1(a,b,m)
    x[a][b]=ran([2,2,2,2,4])
    x[c[0]][c[1]]=ran([2,2,2,2,4])
    return x

#Funcion que devuelve un valor aleatorio de una lista
def ran(m):
    y=random.choice(m)
    return y
#Funcion que evita que se repitan los valores iniciales de la matriz
def ran1(a,b,m):
    a2=ran(m)
    b2=ran(m)
    if(a==a2 and b==b2):
        return ran1(a,b,m)
    else:
        return [a2,b2]
#Funcion que genera el nuevo valor despues de un movimiento
def ran2(x,m,c,d):
    c=ran(m)
    d=ran(m)
    if(x[c][d]==0):
        return [c,d]
    else:
        return ran2(x,m,0,0)

#Funcion encargada de mover y sumar las casillas, y la puntuacion
#h=puntuacion
#Up: x, i=0, j=0, a=1, b=0, c=1, d=0, p=2, y=0, z=0
#Down: x, i=3, j=0, a=-1, b=0, c=1, d=0, p=1, y=0, z=0
#Left: x, i=0, j=0, a=0, b=1, c=0, d=1, p=2, y=1, z=0 
#Right: x, i=0, j=3, a=0, b=-1, c=0, d=1, p=1, y=1, z=0
def suma(x,i,j,a,b,c,d,p,y,z,h):
    if(4>=j+1 and 4>=i+1):
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
        elif(z<7):
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
        
#Funcion que define al objeto principal (game)     
def main():
    x=gam()
    ve = Tk()
    game = App(ve,x)
        
if __name__ == '__main__':
    main()
