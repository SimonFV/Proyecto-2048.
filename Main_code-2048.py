#Proyecto Juego 2048
#Simon Fallas Villalobos


import random

#Matriz inicial del juego y la funcion random para generar sus 2 numeros iniciales.
def gam():
    x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=[0,1,2,3]
    a=ran(m)
    b=ran(m)
    c=ran1(a,b,m)
    x[a][b]=ran([2,2,2,2,4])
    x[c[0]][c[1]]=ran([2,2,2,4])
    
    print("",x[0],"\n",x[1],"\n",x[2],"\n",x[3])

#Función que escoje un valor aleatorio de una lista.
def ran(m):
    y=random.choice(m)
    return y
#Funcion que se asegura que no se repitan las casillas de la matriz inicial.
def ran1(a,b,m):
    a2=ran(m)
    b2=ran(m)
    if(a==a2 and b==b2):
        return ran1(a,b,m)
    else:
        return [a2,b2]

#Función encargada de mover las casillas de la matriz según los parámetros ingresados.
#Suma: h==0, Multiplicacion: h!=0
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
            if(h==0):
                x[i][j]=x[i][j]+x[i][j]
            else:
                x[i][j]=x[i][j]*x[i][j]
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
            return x
    else:
        if(p!=j):
            return suma(x,0,j+b,a,b,c,d,p,y,z,h)
        elif(z<3):
            if(p==2):
                return suma(x,0,0,a,b,c,d,p,y,z+1,h)
            else:
                return suma(x,0,3,a,b,c,d,p,y,z+1,h)
        else:
            return x
        
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
