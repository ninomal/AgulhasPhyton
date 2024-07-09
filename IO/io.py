from tkinter import *
import random

class IO:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Diario")
        self.windows.config(padx= 50, pady= 50)
        self.canvasImage()
        self.labels()
        self.entrys()
        self.button()
        
    def canvasImage(self):
        self.canvas = Canvas(height=300, width=600)
        self.canvas.grid(row= 0, column= 0)
        self.logo_img = PhotoImage(file= self.randomImagem())
        self.canvas.create_image(100, 100, image = self.logo_img)
        
    
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = f"IO\image\ess{randInt}.png"
        print(path)
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
        self.FINURAS_ENTRY.grid(row=3, column=1)
        self.AGULHAS_ENTRY = Entry(width= 20)
        self.AGULHAS_ENTRY.grid(row=4, column=1)

    def button(self):
        self.ADDBUTTON = Button(text= "Adicionar", width= 17)
        self.ADDBUTTON.grid(row = 5, column= 1)
    

        
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    