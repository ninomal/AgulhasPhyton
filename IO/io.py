from tkinter import *
from tkinter import messagebox
from products.Products import Products
import random

class IO:
    def __init__(self):
        self.products = Products("01", "07")
        self.listData = []
        self.windows = Tk()
        self.windows.title("Diario")
        self.windows.config(padx= 20, pady= 10)
        self.canvasImage()
        self.labels()
        self.entrys()
        self.buttonADD()
        self.radioButon()
        self.clearLIstEntrys()
              
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

    def buttonADD(self):
        self.ADDBUTTON = Button(text= "Adicionar", width= 17, command= self.popADD)
        self.ADDBUTTON.grid(row = 5, column= 1)
    
    def buttonContinue(self):
        pass #here
    
    def buttonPassTurn(self):
        pass  #here
        
    def radioButon(self):
        turnLabel = Label(text= "TURNO:")
        turn = StringVar()
        turn.set("TA")
        ta = Radiobutton(text="TA",variable= turn, value= "TA")
        tb = Radiobutton(text="TB",variable= turn, value= "TB")
        tc = Radiobutton(text="TC",variable= turn, value= "TC")

        turnLabel.grid(row = 1, column=3)
        ta.grid(row=2, column=3)
        tb.grid(row=3, column=3)
        tc.grid(row=4, column=3)  
        return turn
        
    def finurasCheck(self):
        finura = self.FINURAS_ENTRY.get()
        asw = self.products.finuraCheck(finura)
        if not asw:
            self.popFinuras()
        else:
            return True
    
    def popFinuras(self):
        messagebox.showwarning(title="Erro", message= "Finura Errada")
        self.clearLIstEntrys()
               
    def popADD(self):
        finuras = self.finurasCheck()
        if finuras :
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
        return self.listData.append([dia, mes, finura, agulha])
    
    def clearLIstEntrys(self):
        self.listData = []
        self.DIA_ENTRY.delete(0, END)
        self.MES_ENTRY.delete(0, END)
        self.FINURAS_ENTRY.delete(0, END)
        self.AGULHAS_ENTRY.delete(0, END)
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    