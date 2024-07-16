from customtkinter import *
from products.Products import Products
from PIL import Image
import random

class IO:
    def __init__(self):
        self.conts = 0
        self.contsAdd = 0
        self.products = Products("01", "07")
        self.listData = []
        self.windows = CTk()
        self.windows.geometry("700x700")
        self.windows.title("Diario")
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        self.buttonADD()
        #self.popFinuras()
        #self.canvasImage()
        self.labels()
        self.entrys()
        self.buttonADD()
        self.radioButon()
        self.buttonContinue()
        self.buttonPassTurn()
        self.frame1()
        #self.clearLIstEntrys()
           
    def frame1(self):
        frame = CTkFrame(master= self.windows, bg_color="white")
        frame.pack(expand ="true", fill = "both", padx = 120, pady = 150, side = LEFT)      
           
    def buttonForme(self, name, comandFunc):
        self.button = CTkButton(text=f"{name}",hover_color="#C850C0",
                                border_color="#FFCC70", border_width=2,
                                master= self.windows , command= comandFunc)  
        return self.button        
    """                      
    def canvasImage(self):
        self.windows1 = CTk()
        self.windows1.geometry("300x300")
        logo_img = Image.open(self.randomImagem())
        canvas = CTkImage(dark_image= logo_img, light_image= logo_img, size=(650,640))
        self.canvas = CTkLabel(master=self.windows1, text="", image= canvas).pack(expand=True,fill="both", side="left")
        
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = f"IO\image\ess{randInt}.png"
        return path
    """
    def labelsForme(self, text):
        label = CTkLabel(master=self.windows, text= f"{text}", bg_color='transparent')
        return label
    
    def labels(self):
        self.diaLabel = self.labelsForme("Dia:")
        self.diaLabel.pack(padx= 20, pady =20)
        self.mes = self.labelsForme("Mês:")
        self.mes.place(relx=0.76, rely=0.54,anchor="e")
        self.finura = self.labelsForme("Finura:")
        self.finura.place(relx=0.76, rely=0.60,anchor="e")
        self.agulhas = self.labelsForme("Agulhas quebradas:")
        self.agulhas.place(relx=0.76, rely=0.66,anchor="e")
        
    def entrys(self):
        self.dia_entry = CTkEntry(master= self.windows, width= 150)
        self.dia_entry.place(relx=0.980, rely=0.48,anchor="e")
        self.mes_entry = CTkEntry(master= self.windows, width= 150)
        self.mes_entry.place(relx=0.980, rely=0.54,anchor="e")
        self.finuras_entry = CTkEntry(master= self.windows, width= 150)
        self.finuras_entry.place(relx=0.980, rely=0.60,anchor="e")
        self.agulhas_entry = CTkEntry(master= self.windows, width= 150)
        self.agulhas_entry.place(relx=0.980, rely=0.66,anchor="e")

    def buttonADD(self): 
        self.addButton = self.buttonForme("Adicionar", comandFunc= self.popADD)
        self.addButton.place(relx=0.4, rely=0.6,anchor="w")
        
    def buttonContinue(self):
        self.continueButton = self.buttonForme("Adicionar mais",comandFunc= self.clearLIstEntrys )
        self.continueButton.place(relx=0.4, rely=0.7,anchor="w")
        
    def buttonPassTurn(self):  
        self.passTurn = self.buttonForme("Passar o turno", comandFunc= self.passTurnFunc)
        self.passTurn.place(relx=0.4, rely=0.7,anchor="e")
        
    def passTurnFunc(self):
        self.conts += 1
        self.clearLIstEntrys()
        if self.conts == 1:
            self.turn.set("TB")
        else:
            self.turn.set("TC")
            self.conts = 0
         
    def radioButon(self):
        self.turn = CTkComboBox(master= self.windows, values=['TA', 'TB', 'TC'])
        self.turn.place(relx=0.980, rely=0.4,anchor="e")      
        return self.turn
              
    def finurasCheck(self):
        finura = self.finuras_entry.get()
        asw = self.products.finuraCheck(finura)
        if not asw:
            self.popFinuras()
        else:
            return asw
    
    def popFinuras(self):
        masterPoP = CTk()
        masterPoP.geometry("300x200")
        messagebox = CTkLabel(master= masterPoP, text= "Finura Errada")
        #messagebox.pack(padx=20, pady=20)
        
        #self.clearLIstEntrys()
    
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Clicar em Adicionar mais ou Passar o turno")
                            
    def popADD(self):
        self.contsAdd +=1
        finuras = self.finurasCheck()
        if self.contsAdd > 1:
            self.popEraserError()
        elif finuras :
            ask = mensagemBox = CTkInputDialog("Confirmação", 
                                    message= "Confirmar os dados")
            self.askTrue(ask)
            return ask
     
    def askTrue(self, ask):
        if ask == True:
            dia = self.dia_entry.get()   
            mes = self.mes_entry.get()
            finura = self.finuras_entry.get()
            agulhas = self.agulhas_entry.get()
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
    
    
    