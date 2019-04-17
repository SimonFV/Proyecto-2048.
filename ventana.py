from tkinter import *
from tkinter import ttk, font
#Borders: "flat", "raised", "sunken", "ridge", "solid", "groove"

class Aplicacion():
    def __init__(self):
        
        self.ve = Tk()
        self.ve.geometry('520x460')
        self.ve.configure(bg = 'grey')
        self.ve.title('2048!!')

        
        self.gr = ttk.Frame(self.ve, padding=(5,5))
        self.gr2 = ttk.Frame(self.ve, padding=(5,5))
        self.gr3 = ttk.Frame(self.ve, padding=(5,5))
        self.gr4 = ttk.Frame(self.ve, padding=(5,5))

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
        #Labels de la matriz del juego
        self.ma00=Label(self.gr, text="0", bd=1, relief="raised").grid(pady=2, padx=2, row=0, column=0, sticky=(N, S, E, W))
        self.ma01=Label(self.gr, text="64", bd=1, relief="sunken").grid(pady=2, padx=2, row=0, column=1, sticky=(N, S, E, W))
        self.ma02=Label(self.gr, text="2", bd=1, relief="raised").grid(pady=2, padx=2, row=0, column=2, sticky=(N, S, E, W))
        self.ma03=Label(self.gr, text="16", bd=1, relief="sunken").grid(pady=2, padx=2, row=0, column=3, sticky=(N, S, E, W))
        self.ma10=Label(self.gr, text="0", bd=1, relief="raised").grid(pady=2, padx=2, row=1, column=0, sticky=(N, S, E, W))
        self.ma11=Label(self.gr, text="8", bd=1, relief="sunken").grid(pady=2, padx=2, row=1, column=1, sticky=(N, S, E, W))
        self.ma12=Label(self.gr, text="2", bd=1, relief="sunken").grid(pady=2, padx=2, row=1, column=2, sticky=(N, S, E, W))
        self.ma13=Label(self.gr, text="4", bd=1, relief="raised").grid(pady=2, padx=2, row=1, column=3, sticky=(N, S, E, W))
        self.ma20=Label(self.gr, text="0", bd=1, relief="sunken").grid(pady=2, padx=2, row=2, column=0, sticky=(N, S, E, W))
        self.ma21=Label(self.gr, text="128", bd=1, relief="raised").grid(pady=2, padx=2, row=2, column=1, sticky=(N, S, E, W))
        self.ma22=Label(self.gr, text="2", bd=1, relief="sunken").grid(pady=2, padx=2, row=2, column=2, sticky=(N, S, E, W))
        self.ma23=Label(self.gr, text="256", bd=1, relief="raised").grid(pady=2, padx=2, row=2, column=3, sticky=(N, S, E, W))
        self.ma30=Label(self.gr, text="0", bd=1, relief="sunken").grid(pady=2, padx=2, row=3, column=0, sticky=(N, S, E, W))
        self.ma31=Label(self.gr, text="0", bd=1, relief="raised").grid(pady=2, padx=2, row=3, column=1, sticky=(N, S, E, W))
        self.ma32=Label(self.gr, text="2", bd=1, relief="sunken").grid(pady=2, padx=2, row=3, column=2, sticky=(N, S, E, W))
        self.ma33=Label(self.gr, text="8", bd=1, relief="raised").grid(pady=2, padx=2, row=3, column=3, sticky=(N, S, E, W))

        self.gr2.grid(column=1, row=0, padx=5, pady=5, sticky=(N, S, E, W))
        self.gr.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
        self.gr3.grid(column=0, row=0, padx=5, pady=5, rowspan=2, sticky=(N, S, E, W))
        self.gr4.grid(column=0, row=2, padx=5, pady=5, columnspan=2, sticky=(N, S, E, W))
        
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
        


        self.ve.mainloop()

        
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
