#Proyecto Juego 2048
#Simon Fallas Villalobos

#Librerias importadas
from tkinter import Tk
from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox
import random
import copy

#Clase que encierra todos los elementos de la interfaz.
class App():
    #Metodo que inicializa el objeto
    #master=parametro de la ventana principal
    def __init__(self, master):
        
        self.ve = master #Ventana principal
        #Configuracion de la ventana
        self.ve.geometry("620x500")
        self.ve.configure(bg = "gray70")
        self.ve.title("2048!!")
        
        #Variables para las fuentes de algunos textos.
        tafont=font.Font(size = 12,weight = "bold") 
        infont=font.Font(size = 10,weight = "bold")
        mafont=font.Font(size = 16,weight = "bold")
        
        self.r="sunken" #Bordes: "flat", "raised", "sunken", "ridge", "solid", "groove"
        self.c="gray40" #Color de las casillas de la matriz
        
        #Determina en que estado esta la interfaz, que se puede hacer y que no
        self.run=0 #0:Selc_usuario, 1,2,8,10,16: Selc_base, 2:bin, 8:oct, 10:dec, 16:hexa
        
        self.seg=1    #Segundos del cronometro
        self.min=5    #Minutos del cronometro
        self.puntos=0     #Puntuacion de la partida
        self.x=[]       #Matriz principal del juego

        #Frames donde se posicionan todos los widgets del juego
        self.gr = ttk.Frame(self.ve, padding=(2,2))     #Frame para la matriz
        self.gr2 = ttk.Frame(self.ve, padding=(2,2))    #Frame para el usuario
        self.gr3 = ttk.Frame(self.ve, padding=(2,2))    #Frame para la tabla de puntuaciones
        self.gr4 = ttk.Frame(self.ve, padding=(2,2))    #Frame para la informacion y las opciones de base
        #Configuracion de los Frames
        self.gr.grid(column=1, row=1, padx=2, pady=2, sticky=(N, S, E, W))
        self.gr2.grid(column=1, row=0, padx=2, pady=2, sticky=(N, S, E, W))
        self.gr3.grid(column=0, row=0, padx=2, pady=2, rowspan=2, sticky=(N, S, E, W))
        self.gr4.grid(column=0, row=2, padx=2, pady=2, columnspan=2, sticky=(N, S, E, W))
        
        #Labels de la puntuacion
        Label(self.gr4, text="PUNTOS: ").grid(pady=2, padx=2, row=1, column=2, sticky=(E))
        self.points = Label(self.gr4, text=self.puntos)
        self.points.grid(pady=2, padx=2, row=1, column=3, sticky=(W))
        #Labels del tiempo
        Label(self.gr4, text="TIEMPO: ").grid(pady=2, padx=2, row=1, column=4, sticky=(E))
        self.tiempo=Label(self.gr4, text="0:00")
        self.tiempo.grid(pady=2, padx=2, row=1, column=5, sticky=(W))
        #Label de informacion
        self.info=Label(self.gr4)
        self.info.grid(pady=2, padx=2, row=0, column=2, columnspan=4, sticky=(W,E))

        #Botones para escojer el modo de juego
        self.bi=Button(self.gr4, command=lambda : self.base(2), text="BINARIO",bg="gray60")
        self.bi.grid(pady=2, padx=2, row=0, column=0, sticky=(E, W))
        self.oc=Button(self.gr4, command=lambda : self.base(8), text="OCTAL",bg="gray60")
        self.oc.grid(pady=2, padx=2, row=1, column=0, sticky=(E, W))
        self.de=Button(self.gr4, command=lambda : self.base(10), text="DECIMAL",bg="gray60")
        self.de.grid(pady=2, padx=2, row=0, column=1, sticky=(E, W))
        self.he=Button(self.gr4, command=lambda : self.base(16), text="HEXADECIMAL",bg="gray60")
        self.he.grid(pady=2, padx=2, row=1, column=1, sticky=(E, W))
        
        #Labels de la tabla de puntuaciones
        #La informacion de la tabla se obtiene de un texto
        self.score=open("Puntuaciones.txt", "r")
        self.sc=self.score.readlines()
        self.records=Label(self.gr3, text="RECORDS",font=tafont)
        self.records.grid(pady=2, padx=2, row=0, column=0,columnspan=2, sticky=(N, S, E, W))
        self.tabla(0)
        self.score.close()
        
        #Labels de la matriz inicial
        self.ma00=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma00.grid(pady=4, padx=4, row=0, column=0, sticky=(N, S, E, W))
        self.ma01=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma01.grid(pady=4, padx=4, row=0, column=1, sticky=(N, S, E, W))
        self.ma02=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma02.grid(pady=4, padx=4, row=0, column=2, sticky=(N, S, E, W))
        self.ma03=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma03.grid(pady=4, padx=4, row=0, column=3, sticky=(N, S, E, W))
        self.ma10=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma10.grid(pady=4, padx=4, row=1, column=0, sticky=(N, S, E, W))
        self.ma11=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma11.grid(pady=4, padx=4, row=1, column=1, sticky=(N, S, E, W))
        self.ma12=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma12.grid(pady=4, padx=4, row=1, column=2, sticky=(N, S, E, W))
        self.ma13=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma13.grid(pady=4, padx=4, row=1, column=3, sticky=(N, S, E, W))
        self.ma20=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma20.grid(pady=4, padx=4, row=2, column=0, sticky=(N, S, E, W))
        self.ma21=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma21.grid(pady=4, padx=4, row=2, column=1, sticky=(N, S, E, W))
        self.ma22=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma22.grid(pady=4, padx=4, row=2, column=2, sticky=(N, S, E, W))
        self.ma23=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma23.grid(pady=4, padx=4, row=2, column=3, sticky=(N, S, E, W))
        self.ma30=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma30.grid(pady=4, padx=4, row=3, column=0, sticky=(N, S, E, W))
        self.ma31=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma31.grid(pady=4, padx=4, row=3, column=1, sticky=(N, S, E, W))
        self.ma32=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma32.grid(pady=4, padx=4, row=3, column=2, sticky=(N, S, E, W))
        self.ma33=Label(self.gr, text="0", bd=2, relief=self.r, bg = self.c, font=mafont)
        self.ma33.grid(pady=4, padx=4, row=3, column=3, sticky=(N, S, E, W))
        
        #Ingresar el usuario
        Label(self.gr2, text="USUARIO: ").grid(pady=5, padx=5, row=0, column=0, sticky=(E, W))
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

        #Loop de la interfaz
        self.ve.mainloop()
    
    #Metodo que construye los Labels de la matriz del juego
    def construir(self):
        b=self.run
        self.forma(0,0)
        self.ma00.configure(text=conv(self.x[0][0],b), relief=self.r, bg = self.c)
        self.forma(0,1)
        self.ma01.configure(text=conv(self.x[0][1],b), relief=self.r, bg = self.c)
        self.forma(0,2)
        self.ma02.configure(text=conv(self.x[0][2],b), relief=self.r, bg = self.c)
        self.forma(0,3)
        self.ma03.configure(text=conv(self.x[0][3],b), relief=self.r, bg = self.c)
        self.forma(1,0)
        self.ma10.configure(text=conv(self.x[1][0],b), relief=self.r, bg = self.c)
        self.forma(1,1)
        self.ma11.configure(text=conv(self.x[1][1],b), relief=self.r, bg = self.c)
        self.forma(1,2)
        self.ma12.configure(text=conv(self.x[1][2],b), relief=self.r, bg = self.c)
        self.forma(1,3)
        self.ma13.configure(text=conv(self.x[1][3],b), relief=self.r, bg = self.c)
        self.forma(2,0)
        self.ma20.configure(text=conv(self.x[2][0],b), relief=self.r, bg = self.c)
        self.forma(2,1)
        self.ma21.configure(text=conv(self.x[2][1],b), relief=self.r, bg = self.c)
        self.forma(2,2)
        self.ma22.configure(text=conv(self.x[2][2],b), relief=self.r, bg = self.c)
        self.forma(2,3)
        self.ma23.configure(text=conv(self.x[2][3],b), relief=self.r, bg = self.c)
        self.forma(3,0)
        self.ma30.configure(text=conv(self.x[3][0],b), relief=self.r, bg = self.c)
        self.forma(3,1)
        self.ma31.configure(text=conv(self.x[3][1],b), relief=self.r, bg = self.c)
        self.forma(3,2)
        self.ma32.configure(text=conv(self.x[3][2],b), relief=self.r, bg = self.c)
        self.forma(3,3)
        self.ma33.configure(text=conv(self.x[3][3],b), relief=self.r, bg = self.c)
        

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
        elif(self.x[i][j]==1024):
            self.c="yellow"
        elif(self.x[i][j]==2048):
            self.c="magenta"
        elif(self.x[i][j]==4096):
            self.c="deeppink"
        else:
            self.c="red"

    #Metodo que escoge la base para jugar
    def base(self,b):
        if(self.run==1):
            #Inicia el cronometro
            self.crono()
        if(self.run!=0):
            if(b==2):
                self.run=2
                self.bi.configure(bg="yellow")
                self.oc.configure(bg="gray60")
                self.de.configure(bg="gray60")
                self.he.configure(bg="gray60")
            elif(b==8):
                self.run=8
                self.bi.configure(bg="gray60")
                self.oc.configure(bg="dodgerblue")
                self.de.configure(bg="gray60")
                self.he.configure(bg="gray60")
            elif(b==10):
                self.run=10
                self.bi.configure(bg="gray60")
                self.oc.configure(bg="gray60")
                self.de.configure(bg="lawngreen")
                self.he.configure(bg="gray60")
            elif(b==16):
                self.run=16
                self.bi.configure(bg="gray60")
                self.oc.configure(bg="gray60")
                self.de.configure(bg="gray60")
                self.he.configure(bg="tomato2")
            self.info.configure(text="MUEVA LAS CASILLAS CON LAS FLECHAS",bg = "skyblue")
            #Construye los Labels de la matriz del juego
            self.construir()
     
    #Metodo que ejecuta la funcion indicada segun el movimiento recibido del teclado
    def funcMove(self,event):
        if(self.run==2 or self.run==8 or self.run==10 or self.run==16):
            if(event.keysym=="Up"): 
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,0,0,1,0,1,0,2,0,0,0))
            elif(event.keysym=="Down"):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,3,0,-1,0,1,0,1,0,0,0))
            elif(event.keysym=="Left"):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,0,0,0,1,0,1,2,0,0,0))
            elif(event.keysym=="Right"):
                z=copy.deepcopy(self.x)
                d = copy.deepcopy(suma(self.x,0,3,0,-1,0,1,1,0,0,0))  
            self.x = d[0]
            self.puntos = self.puntos + d[1]
            p=copy.deepcopy(ran2(self.x))
            if(self.x!=z):
                if(d[2]==2048):
                    self.info.configure(text="¡LO HAS CONSEGUIDO, FELICIDADES!",bg = "springgreen1")
                if(p!=0):
                    self.x[p[0]][p[1]]=ran([2,2,2,2,2,4])
                    self.construir()
                    self.points.configure(text=self.puntos)
                if(gameover(self.x,0,0,0)==False):
                    self.run=0
                    self.info.configure(text="NO HAY MAS MOVIMIENTOS",bg = "salmon")
                    self.save_text()
                    self.seg=1
                    self.min=5
                    self.puntos=0

    #Metodo que crea la tabla de records
    def tabla(self,b):
        if(b<19):
            Label(self.gr3, text=self.sc[b][:-1]).grid(pady=2, padx=2, row=b+1, column=0, sticky=(N, S, E, W))
            Label(self.gr3, text=self.sc[b+1][:-1], bd=2, relief="ridge").grid(pady=2, padx=2, row=b+1, column=1, sticky=(N, S, E, W))
            self.tabla(b+2)

    #Metodo que guarda el usuario
    def user(self):
        if(self.run==0 or self.run==1):
            self.info.configure(text="INGRESE UN NOMBRE DE JUGADOR",bg = "white")
            self.entry.configure(state="normal")
            Button(self.gr2, command=self.user_get, text="ACEPTAR").grid(pady=2, padx=2, row=0, column=2, sticky=(E, W))
        else:
            MsgBox = messagebox.askquestion ('Cambiar Usuario','Si cambia de usuario terminara la partida actual.',icon = 'warning')
            if(MsgBox=='yes'):
                self.save_text()
                self.puntos=0
                self.x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                self.construir()
                self.seg=1
                self.min=5
                self.tiempo.configure(text="0:00")
                self.points.configure(text="0")
                self.run=0
                self.user()
        
    #Metodo que guarda el usuario e inicia el juego
    def user_get(self):
        #Reccoje el nombre ingresado
        self.name=self.entry.get()
        if(self.name!=""):
            #Se crea la matriz con los valores aleatorios iniciales
            self.x=gam()
            self.run=1
            self.cambiar_user()
        
    #Metodo que permite cambiar el usuario
    def cambiar_user(self):
        Label(self.gr2, text="USUARIO: ").grid(pady=5, padx=5, row=0, column=0, sticky=(E, W))
        self.entry.configure(state="readonly")
        Button(self.gr2, command=self.user, text="CAMBIAR").grid(pady=2, padx=2, row=0, column=2, sticky=(E, W))
        self.points.configure(text=self.puntos)
        self.tiempo.configure(text="0:00")
        self.info.configure(text="ESCOJA UNA BASE PARA INICIAR",bg = "khaki")

    #Metodo que presenta el cronometro
    def crono(self):
        if(self.run!=0):
            if(self.min!=0 or self.seg!=0):
                if(self.seg>0):
                    self.seg=self.seg-1
                    if(self.seg<10):
                        self.tiempo.configure(text=str(self.min)+":0"+str(self.seg))
                    else:
                        self.tiempo.configure(text=str(self.min)+":"+str(self.seg))
                    self.tiempo.after(1000, self.crono)
                else:
                    self.seg=59
                    self.min=self.min-1
                    self.tiempo.configure(text=str(self.min)+":"+str(self.seg))
                    self.tiempo.after(1000, self.crono)
            else:
                self.save_text()
                self.puntos=0
                self.seg=1
                self.min=5
                self.run=0
                self.info.configure(text="SE ACABO EL TIEMPO",bg = "salmon")
                
    #Metodo que guarda la puntuacion final en el texto y la presenta en la tabla
    #el valor de m determina en que posicion esta el usuario en la tabla, o si no existe.
    def save_text(self):
        self.score=open("Puntuaciones.txt", "w")
        self.score.write("")
        self.score.close()
        self.score=open("Puntuaciones.txt", "a")
        m=self.name_repet(0,21)
        if(m==21):
            self.comp_name(0)
        else:
            self.posic_name(m)
        self.escr_name(0)
        self.score.close()
        self.score=open("Puntuaciones.txt", "r")
        self.sc=self.score.readlines()
        self.tabla(0)
        self.score.close()
    #Pregunta si el nombre ya esta en la lista
    #b es la posicion en la lista que guarda los datos de la tabla
    def name_repet(self,b,m):
        if(b<19):
            if(self.sc[b][:-1]==self.name):
                m=b
            else:
                return self.name_repet(b+2,m)
        return m
    #Si el usuario existe, lo reposiciona
    def posic_name(self,b):
        if(int(self.sc[b+1][:-1])<=self.puntos):
            if(b!=0):
                if(self.puntos>int(self.sc[b-1][:-1])):
                    self.sc[b]=self.sc[b-2]
                    self.sc[b+1]=self.sc[b-1]
                    self.sc[b-2]=str(self.name)+'\n'
                    self.sc[b-1]=str(self.puntos)+'\n'
                    self.posic_name(b-2)
                else:
                    self.sc[b]=str(self.name)+'\n'
                    self.sc[b+1]=str(self.puntos)+'\n'
            else:
                self.sc[b]=str(self.name)+'\n'
                self.sc[b+1]=str(self.puntos)+'\n'
    #Si el usuario no existe, lo ingresa en la posicion correcta
    def comp_name(self,b):
        if(b<19):
            if(int(self.sc[b+1][:-1])<self.puntos):
                self.mover_name(18,b)
                self.sc[b]=str(self.name)+'\n'
                self.sc[b+1]=str(self.puntos)+'\n'
            else:
                self.comp_name(b+2)
    #Reacomoda las casillas siguientes a la ingresada         
    def mover_name(self,b,m):
        if(b>m):
            self.sc[b]=self.sc[b-2]
            self.sc[b+1]=self.sc[b-1]
            self.mover_name(b-2,m)
    #Escribe los datos de la tabla en el texto
    def escr_name(self,b):
        if(b<19):
            self.score.write(self.sc[b])
            self.score.write(self.sc[b+1])
            self.escr_name(b+2)
            
            
######PARTE LOGICA DE LA MATRIZ DEL JUEGO########

#Crea la matriz inicial del juego x con los dos valores aleatorios.
def gam():
    x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=[0,1,2,3]
    a=ran(m) #valores filas y columnas de la primera posicion
    b=ran(m)
    c=ran1(a,b,m)  #segundo valor diferente al primero
    x[a][b]=ran([2,2,2,2,2,4])
    x[c[0]][c[1]]=ran([2,2,2,2,2,4])
    return x
#Escoje un valor aleatorio de una lista
def ran(m):
    y=random.choice(m)
    return y
#Escoje un valor aleatorio distinto al primero
def ran1(a,b,m):
    a2=ran(m)
    b2=ran(m)
    if(a==a2 and b==b2):
        return ran1(a,b,m)
    else:
        return [a2,b2]
   
#Escoje un valor aleatorio entre las casillas que quedan como 0
def ran2(x):
    c=[]
    c=zero(x,0,0,c)
    if(len(c)>0):
        d=ran(c)
        return [int(d[0]),int(d[1])]
    else:
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

#Funcion encargada de mover las casillas y sumar la puntuacion, tambien determina si se llega a 2048:

#x=matriz, h=puntuacion, g=devuelve 2048 cuando la suma de dos casillas de ese valor.
#i y j son los valores de las filas y columnas.
#a, b, c y d son valores que se suman a i y j para moverse por la matriz dependiendo del movimiento.
#p determina cuando debe parar el recorrido despues de que se evalua hasta la tercera fila o columna.
#P y d tambien se utilizan para determinar cual movimiento se esta realizando y asi tomar una ruta especifica.
#z determina el numero de repeticiones que se hacen para mover todas las casillas desde un extremo a otro,
# además, determina cuando se deben sumar las casillas o cuando se mueven unicamente.
#Up: x, i=0, j=0, a=1, b=0, c=1, d=0, p=2, z=0, h=0, g=0
#Down: x, i=3, j=0, a=-1, b=0, c=1, d=0, p=1, z=0, h=0, g=0
#Left: x, i=0, j=0, a=0, b=1, c=0, d=1, p=2, z=0, h=0, g=0
#Right: x, i=0, j=3, a=0, b=-1, c=0, d=1, p=1, z=0, h=0, g=0
def suma(x,i,j,a,b,c,d,p,z,h,g):
    if(3>=j and 3>=i):
        if(x[i][j]==0 and z!=2):
            x[i][j]=x[i+a][j+b]
            x[i+a][j+b]=0
        elif(x[i][j]==x[i+a][j+b] and z==2):
            h=h+x[i][j]+x[i][j]
            x[i][j]=x[i][j]+x[i][j]
            if(x[i][j]==2048):
                g=2048
            x[i+a][j+b]=0
        return suma(x,i+d,j+c,a,b,c,d,p,z,h,g)
    elif(d==0):
        if(p!=i):
            return suma(x,i+a,0,a,b,c,d,p,z,h,g)
        elif(z<3):
            if(p==2):
                return suma(x,0,0,a,b,c,d,p,z+1,h,g)
            else:
                return suma(x,3,0,a,b,c,d,p,z+1,h,g)
        else:
            return [x,h,g]
    else:
        if(p!=j):
            return suma(x,0,j+b,a,b,c,d,p,z,h,g)
        elif(z<3):
            if(p==2):
                return suma(x,0,0,a,b,c,d,p,z+1,h,g)
            else:
                return suma(x,0,3,a,b,c,d,p,z+1,h,g)
        else:
            return [x,h,g]
                
#Funcion que determina si todavia quedan movimientos
#x es la matriz, i y j sus filas y columnas, z determina la direccion en que se evalua.
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

#Funcion que convierte de decimal a base binaria, octal o hexadecimal     
# x=int, b=base(2,8,16)
def conv(x,b):
    if(x>b-1):
        if(x%b==10):
            return conv(x//b,b) + "A"
        elif(x%b==11):
            return conv(x//b,b) + "B"
        elif(x%b==12):
            return conv(x//b,b) + "C"
        elif(x%b==13):
            return conv(x//b,b) + "D"
        elif(x%b==14):
            return conv(x//b,b) + "E"
        elif(x%b==15):
            return conv(x//b,b) + "F"
        else:
            return conv(x//b,b) + str(x%b)
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
     
#Funcion principal que define la variable de la ventana y define la clase del objeto.
def main():
    ve = Tk()
    game = App(ve)
    return 0

if __name__ == '__main__':
    main()
