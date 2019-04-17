#Proyecto Juego 2048
#Simon Fallas Villalobos

#Matriz inicial del juego y la funcion random para generar sus 2 numeros iniciales.

import random

def gam():
    x=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=[0,1,2,3]
    a=ran(m)
    b=ran(m)
    c=ran1(a,b,m)
    x[a][b]=ran([2,2,2,2,4])
    x[c[0]][c[1]]=ran([2,2,2,4])
    
    print("",x[0],"\n",x[1],"\n",x[2],"\n",x[3])

def ran(m):
    y=random.choice(m)
    return y
def ran1(a,b,m):
    a2=ran(m)
    b2=ran(m)
    if(a==a2 and b==b2):
        return ran1(a,b,m)
    else:
        return [a2,b2]
