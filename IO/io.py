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
        self.frame1()
        self.buttonPainel()
        self.frameButton2()
        self.canvasImage()
        self.firma()
        
        self.clearLIstEntrys()
        
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=820, y=791, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=251, height=276, background="#4A1985")
        self.anchorPane.place(x=55, y=64) 
        
        month_label = tk.Label(self.anchorPane, text="Mês:", font=("Helvetica", 21),
                               bg="#4A1985")
        month_label.place(x=29, y=14, width=54, height=31)
        
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

        self.monthEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.monthEntry.place(x=89, y=17, width=45, height=25)

        dayInit = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        dayInit.place(x=89, y=48, width=45, height=25)

        self.dayEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.dayEntry.place(x=120, y=144, width=81, height=26)

        self.finuraEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.finuraEntry.place(x=120, y=185, width=81, height=26)

        self.agulhaEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.agulhaEntry.place(x=120, y=228, width=81, height=26)
        
        combo_setor = ttk.Combobox(self.anchorPane, values=["Raschell", "Jacquard", "ketten"],
                                   font=("Helvetica", 14), background= "#A580CA", foreground="#A580CA")
        combo_setor.place(x=21, y=92, width=87, height=25)
        combo_setor.set("Setor")

        combo_turno = ttk.Combobox(self.anchorPane, values=["TA", "TB", "TC"],
                                   font=("Helvetica", 14), background= "#A580CA", foreground="#A580CA")
        combo_turno.place(x=142, y=92, width=87, height=25)  
        combo_turno.set("Turno")      
        self.comboTurno()
        self.comboxSetor()
                          
    def canvasImage(self): 
        image_frame = Canvas(self.windows, width=406, height=400, background="#080121")
        image_frame.place(x=742, y=378)
        self.logo_img = PhotoImage(file= self.randomImagem())
        image_frame.create_image(100, 100, image = self.logo_img)
        
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = f"IO\image\ess{randInt}.png"
        return path
            
    def frameButton2(self):
        button_pane = tk.Frame(self.windows, width=410, height=104, background="#4A1985")
        button_pane.place(x=742, y=270)
        button_dia = tk.Button(button_pane, text="Agulhas do Dia", font=("Helvetica", 18),
                               bg="#A580CA", command= "aad")
        button_dia.place(x = 4, y= 4, width=200)
        
        button_graficoPizza = tk.Button(button_pane, text="Grafico pizza",font=("Helvetica", 18),
                                        bg="#A580CA",command= "add")
        button_graficoPizza.place(x= 207 , y= 4, width=200)
        
        button_graficoMes = tk.Button(button_pane, text="Grafico do mês",font=("Helvetica", 18),
                                        bg="#A580CA",command= "add")
        button_graficoMes.place(x= 207 , y= 54, width=200)
        
        button_comparaMes = tk.Button(button_pane, text="Comparar o Mês",font=("Helvetica", 18),
                                        bg="#A580CA",command= "add")
        button_comparaMes.place(x= 4 , y= 54, width=200)
              
    
    def buttonPainel(self):
        button_pane = tk.Frame(self.windows, width=334, height=114, background="#4A1985")
        button_pane.place(x=55, y=352)

        button_add = tk.Button(button_pane, text="Adicionar", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        button_add.place(x=109, y=7, width=130)

        button_skip_turn = tk.Button(button_pane, text="Pular turno", font=("Helvetica", 18),
                                     bg="#A580CA", command= self.passTurnFunc)
        button_skip_turn.place(x=6, y=58)

        button_add_more = tk.Button(button_pane, text="Adicionar + ", font=("Helvetica", 18),
                                    bg="#A580CA",command= self.clearLIstEntrys)
        button_add_more.place(x=179, y=58)
     
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
        
    def monthNotNumber(self):
        monthStr = self.monthEntry.get()
        try:
            month = int(monthStr)
            if type(month) != int or month >=13 or month == None:
                return True
            else:
                return False
        except  ValueError :
            pass
               
    def dayNotnumber(self):
        dayStr = self.dayEntry.get()
        try:
            day = int(dayStr)
            if type(day) != int or day >=32 or day == None:
                return True
            else:
                return False
        except  ValueError :
            pass
              
    def agulhaNotNumber(self):
        agulhaStr = self.agulhaEntry.get()
        try:
            agulha = int(agulhaStr)
            if type(agulha) != int or agulha == None:
                return True
            else:
                return False
        except ValueError:
            pass
            
    def popValueError(self):
        masterPoP = Tk()
        masterPoP.geometry("300x200")
        messagebox = tk.Label(master= masterPoP, text= "Valor invalido")
        messagebox.pack(padx= 40, pady= 40)   
        self.agulhaEntry.delete(0, END)
        self.dayEntry.delete(0, END)
        self.monthEntry.delete(0, END)
        self.listData = []
        self.contsAdd = 0
            
    def popAgulhaErrada(self):
        masterPoP = Tk()
        masterPoP.geometry("300x200")
        messagebox = tk.Label(master= masterPoP, text= "Agulha invalida")
        messagebox.pack(padx= 40, pady= 40)   
        self.agulhaEntry.delete(0, END)
        self.contsAdd = 0
               
    def popDay(self):
        masterPoP = Tk()
        masterPoP.geometry("300x200")
        messagebox = tk.Label(master= masterPoP, text= "Dia errado")
        messagebox.pack(padx= 40, pady= 40)   
        self.dayEntry.delete(0, END)
        self.contsAdd = 0
    
    def popFinuras(self):
        masterPoP = Tk()
        masterPoP.geometry("300x200")
        messagebox = tk.Label(master= masterPoP, text= "Finura Errada")
        messagebox.pack(padx=40, pady=40)   
        self.clearLIstEntrys()
        
    def popMonth(self):
        masterPoP = Tk()
        masterPoP.geometry("300x200")
        messagebox = tk.Label(master= masterPoP, text= "Mês INVALIDO")
        messagebox.pack(padx=40, pady=40)   
        self.monthEntry.delete(0, END)
        self.contsAdd = 0
    
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Clicar em Adicionar mais ou Passar o turno")
                               
    def popADD(self):
        self.contsAdd +=1
        finuras = self.finurasCheck()
        if self.contsAdd > 1:
            self.popEraserError()
        elif self.monthNotNumber():
            self.popMonth()
        elif self.dayNotnumber():
            self.popDay()
        elif self.agulhaNotNumber():
            self.popAgulhaErrada()
        elif finuras :
            ask  = messagebox.askyesno("Confirmação", 
                                    message= "Confirmar os dados")
            self.askTrue(ask)
            return ask
     
    def askTrue(self, ask):
        try:
            if ask == True:
                dia = int(self.dayEntry.get())   
                mes = int(self.monthEntry.get())
                finura = self.finuraEntry.get()
                agulhas = int(self.agulhaEntry.get())
                turn = self.combo_turno.get()
                self.addFunc(dia, mes, turn, finura, agulhas)
        except ValueError:
            self.popValueError()
                  
    def addFunc(self, dia, mes, turn, finura , agulha):
        dataList = [dia, mes, turn, finura, agulha]
        list(map(lambda data: self.listData.append(data), dataList))
        return self.listData
       
    def clearLIstEntrys(self):
        self.listData = []
        self.finuraEntry.delete(0, END)
        self.agulhaEntry.delete(0, END)
        self.contsAdd = 0
        
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    