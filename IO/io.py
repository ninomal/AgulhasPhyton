from tkinter import *
from tkinter import messagebox
from products.Products import Products
import random

class IO:
    def __init__(self):
        self.conts = 0
        self.contsAdd = 0
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
        self.buttonContinue()
        self.buttonPassTurn()
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
        self.continueButton = Button(text="Adicionar mais", 
                        width= 17, command= self.clearLIstEntrys )
        self.continueButton.grid(row = 5 , column= 0)
        
    def buttonPassTurn(self):  
        self.passTurn = Button(text="Passar o turno", 
                        width= 17, command=  self.passTurnFunc)
        self.passTurn.grid(row = 5 , column= 2)
        
    def passTurnFunc(self):
        self.conts += 1
        self.clearLIstEntrys()
        if self.conts == 1:
            self.turn.set("TB")
        else:
            self.turn.set("TC")
            self.conts = 0
         
    def radioButon(self):
        turnLabel = Label(text= "TURNO:")     
        self.turn = StringVar()
        self.turn.set("TA")
        ta = Radiobutton(text="TA",variable= self.turn, value= "TA")
        tb = Radiobutton(text="TB",variable= self.turn, value= "TB")
        tc = Radiobutton(text="TC",variable= self.turn, value= "TC")
        turnLabel.grid(row = 1, column=3)
        ta.grid(row=2, column=3)
        tb.grid(row=3, column=3)
        tc.grid(row=4, column=3)       
        return self.turn
              
    def finurasCheck(self):
        finura = self.FINURAS_ENTRY.get()
        asw = self.products.finuraCheck(finura)
        if not asw:
            self.popFinuras()
        else:
            return asw
    
    def popFinuras(self):
        messagebox.showwarning(title="Erro", message= "Finura Errada")
        self.clearLIstEntrys()
    
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Clicar em Adicionar mais ou Passar o turno")
                            
    def popADD(self):
        self.contsAdd +=1
        finuras = self.finurasCheck()
        if self.contsAdd > 1:
            self.popEraserError()
        elif finuras :
            ask = mensagemBox = messagebox.askyesno("Confirmação", 
                                    message= "Confirmar os dados")
            self.askTrue(ask)
            return ask
     
    def askTrue(self, ask):
        if ask == True:
            dia = self.DIA_ENTRY.get()   
            mes = self.MES_ENTRY.get()
            finura = self.FINURAS_ENTRY.get()
            agulhas = self.AGULHAS_ENTRY.get()
            turn = self.turn.get()
            self.addFunc(dia, mes, turn, finura, agulhas)
                  
    def addFunc(self, dia, mes, turn, finura , agulha):
        dataList = [dia, mes, turn, finura, agulha]
        list(map(lambda data: self.listData.append(data), dataList))
        print(self.listData)
        return self.listData
       
    def clearLIstEntrys(self):
        self.listData = []
        #self.DIA_ENTRY.delete(0, END)
        #self.MES_ENTRY.delete(0, END)
        self.FINURAS_ENTRY.delete(0, END)
        self.AGULHAS_ENTRY.delete(0, END)
        self.contsAdd = 0
        
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    