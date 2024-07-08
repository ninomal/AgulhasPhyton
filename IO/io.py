from tkinter import *

class IO:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("Diario")
        self.windows.config(padx= 300, pady= 200)
        #self.canvas = Canvas(height=300, width=300)
        #self.canvas.grid(column=1 , row = 0)
        self.labels()
        self.entrys()
        self.button()
        
        
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
    
    
    