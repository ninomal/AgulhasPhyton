import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from products.Products import Products
from PIL import Image
import random

class IO:
    def __init__(self):
        self.conts = 0
        self.contsAdd = 0
        self.products = Products("01", "07")
        self.listData = []
        self.windows = Tk()
        self.windows.geometry("1156x834")
        self.windows.title("Diario")
        self.windows.config(background="#080121")
        #self.popFinuras()
        self.canvasImage()
        self.buttonADD()
        self.frame1()
        self.buttonContinue()
        self.buttonPassTurn()
        self.firma()
        #self.clearLIstEntrys()
        
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=682, y=777, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=251, height=276, background="#4A1985")
        self.anchorPane.place(x=55, y=64) 
        
        self.monthEntry = tk.Label(self.anchorPane, text="Mês:", font=("Helvetica", 21),
                               bg="#4A1985")
        self.monthEntry.place(x=29, y=14, width=54, height=31)
        
        label_day1 = tk.Label(self.anchorPane, text="Dia:", font=("Helvetica", 21),
                              bg="#4A1985")
        label_day1.place(x=25, y=45, width=53, height=25)
        
        label_day2 = tk.Label(self.anchorPane, text="Dia:", font=("Helvetica", 21)
                              ,bg="#4A1985")
        label_day2.place(x=22, y=141, width=53, height=25)
        
        label_finura = tk.Label(self.anchorPane, text="Finura:", font=("Helvetica", 21),
                                bg="#4A1985")
        label_finura.place(x=20, y=182, width=90, height=31)
        
        self.label_agulha = tk.Label(self.anchorPane, text="Agulha:", font=("Helvetica", 21),
                                bg="#4A1985")
        self.label_agulha.place(x=19, y=225, width=95, height=31)

        month = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        month.place(x=89, y=17, width=45, height=25)

        day1 = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        day1.place(x=89, y=48, width=45, height=25)

        text_day2 = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        text_day2.place(x=120, y=144, width=81, height=26)

        self.finuraEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.finuraEntry.place(x=120, y=185, width=81, height=26)

        self.agulhaEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.agulhaEntry.place(x=120, y=228, width=81, height=26)
        
        combo_setor = ttk.Combobox(self.anchorPane, values=["Raschell", "Jacquard", "ketten"],
                                   font=("Helvetica", 14))
        combo_setor.place(x=21, y=92, width=87, height=25)
        combo_setor.set("Setor")

        combo_turno = ttk.Combobox(self.anchorPane, values=["TA", "TB", "TC"],
                                   font=("Helvetica", 14))
        combo_turno.place(x=142, y=92, width=87, height=25)
        combo_turno.set("Turno")

        month = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        month.place(x=89, y=17, width=45, height=25)

        self.day1 = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.day1.place(x=89, y=48, width=45, height=25)

        self.dayEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.dayEntry.place(x=120, y=144, width=81, height=26)

        text_finura = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        text_finura.place(x=120, y=185, width=81, height=26)

        text_agulha = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        text_agulha.place(x=120, y=228, width=81, height=26)
                   
    def canvasImage(self): 
        image_frame = Canvas(self.windows, width=660, height=658,background="#080121")
        image_frame.place(x=742, y=360)
        logo_img = Image.open(self.randomImagem())
        image_frame.create_image(100, 100, image = logo_img)
        
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = f"IO\image\ess{randInt}.png"
        return path
    
    def buttonPainel(self):
        button_pane = tk.Frame(self.windows, width=334, height=114, background="#4A1985")
        button_pane.place(x=55, y=352)

        button_add = tk.Button(button_pane, text="Adicionar", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        button_add.place(x=120, y=14, width=109)

        button_skip_turn = tk.Button(button_pane, text="Pular turno", font=("Helvetica", 18),
                                     bg="#A580CA", command= self.passTurnFunc)
        button_skip_turn.place(x=6, y=67)

        button_add_more = tk.Button(button_pane, text="Adicionar + ", font=("Helvetica", 18),
                                    bg="#A580CA",command= self.clearLIstEntrys)
        button_add_more.place(x=193, y=67)
     
    def comboxSetor(self):
        combo_setor = ttk.Combobox(self.anchorPane, values=["Raschell", "Jacquard", "ketten"],
                                   font=("Helvetica", 14))
        combo_setor.place(x=21, y=92, width=87, height=25)
        combo_setor.set("Raschell")
        return combo_setor

    def comboTurno(self):
        self.combo_turno = ttk.Combobox(self.anchorPane, values=["TA", "TB", "TC"],
                                   font=("Helvetica", 14))
        self.combo_turno.place(x=142, y=92, width=87, height=25)
        self.combo_turno.set("TA")
        return self.combo_turno
               
    def passTurnFunc(self):
        self.conts += 1
        self.clearLIstEntrys()
        if self.conts == 1:
            self.combo_turno.set("TB")
        else:
            self.combo_turno.set("TC")
            self.conts = 0
                     
    def finurasCheck(self):
        finura = self.finuraEntry.get()
        asw = self.products.finuraCheck(finura)
        if not asw:
            self.popFinuras()
        else:
            return asw
    
    def popFinuras(self):
        masterPoP = Tk()
        masterPoP.geometry("300x200")
        messagebox = tk.Label(master= masterPoP, text= "Finura Errada")
        messagebox.pack(padx=20, pady=20)   
        self.clearLIstEntrys()
    
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Clicar em Adicionar mais ou Passar o turno")
       #messagebox.pack(padx=20, pady=20)  
                            
    def popADD(self):
        self.contsAdd +=1
        finuras = self.finurasCheck()
        if self.contsAdd > 1:
            self.popEraserError()
        elif finuras :
            ask = mensagemBox = tk.Label("Confirmação", 
                                    message= "Confirmar os dados")
            self.askTrue(ask)
            return ask
     
    def askTrue(self, ask):
        if ask == True:
            dia = self.dayEntry.get()   
            mes = self.monthEntry.get()
            finura = self.finuraEntry.get()
            agulhas = self.agulhaEntry.get()
            turn = self.combo_turno.get()
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
        self.finuraEntry.delete(0, END)
        self.agulhaEntry.delete(0, END)
        self.contsAdd = 0
        
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    