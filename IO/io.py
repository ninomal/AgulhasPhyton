from tkinter import *
from tkinter import messagebox
import random

class IO:
    def __init__(self):
        self.listData = []
        self.windows = Tk()
        self.windows.title("Diario")
        self.windows.config(padx= 20, pady= 10)
        self.canvasImage()
        self.labels()
        self.entrys()
        self.button()
              
    def canvasImage(self):
        self.canvas = Canvas(height=300, width=600)
        self.canvas.grid(row= 0, column= 1)
        self.logo_img = PhotoImage(file= self.randomImagem())
        self.canvas.create_image(100, 100, image = self.logo_img)
        
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = f"IO\image\ess{randInt}.png"
        return path
               
    def labels(self):
        self.DIALABEL = Label(text="Dia:")
        self.DIALABEL.grid(row= 1, column= 0)
        self.MES = Label(text= "Mês:")
        self.MES.grid(row = 2, column=0)
        self.FINURA = Label(text= "Finura:")
        self.FINURA.grid(row = 3, column=0)
        self.AGULHAS = Label(text= "Agulhas quebradas:")
        self.AGULHAS.grid(row = 4, column=0)
        
    def entrys(self):
        self.DIA_ENTRY = Entry(width= 20)
        self.DIA_ENTRY.grid(row=1, column= 1)
        self.MES_ENTRY = Entry(width= 20)
        self.MES_ENTRY.grid(row=2, column= 1)
        self.FINURAS_ENTRY = Entry(width= 20)
        self.FINURAS_ENTRY.grid(row=3, column= 1)
        self.AGULHAS_ENTRY = Entry(width= 20)
        self.AGULHAS_ENTRY.grid(row=4, column= 1)

    def button(self):
        self.ADDBUTTON = Button(text= "Adicionar", width= 17, command= self.pop)
        self.ADDBUTTON.grid(row = 5, column= 1)
    
    def pop(self):
        ask = mensagemBox = messagebox.askyesno("Confirmação", message= "Confirmar os dados")
        self.askTrue(ask)
        return ask
     
    def askTrue(self, ask):
        if ask == True:
            dia = self.DIA_ENTRY.get()   
            mes = self.MES_ENTRY.get()
            finura = self.FINURAS_ENTRY.get()
            agulhas = self.AGULHAS_ENTRY.get()
            self.addFunc(dia, mes, finura, agulhas)
                  
    def addFunc(self, dia, mes, finura , agulha):
        return self.listData.extend([dia, mes, finura, agulha])
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    