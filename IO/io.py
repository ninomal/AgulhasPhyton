import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from products.Products import Products
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from functools import cache
from enums.enumsToday import Enumstoday


class IO:
    def __init__(self):
        self.conts = 0
        self.contsAdd = 0
        self.products = Products()
        self.listData = []
        self.dayList = []
        self.windows = Tk()
        self.windows.geometry("1156x834")
        self.windows.title("Diario")
        self.windows.config(background="#080121")
        self.frame1()
        self.buttonPainel()
        self.frameButton2()
        self.canvasImage()
        self.firma()
        self.optionsFrame()
        self.plot_window = None
        self.clearLIstEntrys()
        self.day = 1
        self.month = "1"
        self.GraficsOpen = False
        
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=820, y=791, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=251, height=276,
                                   background="#4A1985")
        self.anchorPane.place(x=55, y=64) 
        
        month_label = tk.Label(self.anchorPane, text="Mês:", font=("Helvetica", 21),
                               bg="#4A1985")
        month_label.place(x=29, y=14, width=54, height=31)
        
        label_day1 = tk.Label(self.anchorPane, text="Dia:", font=("Helvetica", 21),
                              bg="#4A1985")
        label_day1.place(x=25, y=45, width=53, height=25)
          
        label_finura = tk.Label(self.anchorPane, text="Finura:", font=("Helvetica", 21),
                                bg="#4A1985")
        label_finura.place(x=20, y=182, width=90, height=31)
        
        self.label_agulha = tk.Label(self.anchorPane, text="Agulha:",
                                     font=("Helvetica", 21), bg="#4A1985")
        self.label_agulha.place(x=19, y=225, width=95, height=31)

        self.monthEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.monthEntry.place(x=89, y=17, width=45, height=25)

        self.dayEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.dayEntry.place(x=89, y=48, width=45, height=25)

        self.finuraEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.finuraEntry.place(x=120, y=185, width=81, height=26)

        self.agulhaEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        self.agulhaEntry.place(x=120, y=228, width=81, height=26)
        
        combo_setor = ttk.Combobox(self.anchorPane, values=["Raschell",
                                    "Jacquard", "ketten"], font=("Helvetica", 14),
                                   background= "#A580CA", foreground="#A580CA")
        combo_setor.place(x=21, y=92, width=87, height=25)
        combo_setor.set("Setor")

        combo_turno = ttk.Combobox(self.anchorPane, values=["TA", "TB", "TC"],
                                   font=("Helvetica", 14), background= "#A580CA",
                                   foreground="#A580CA")
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
        path = self.products.randImage()
        return path
                                     
    def frameButton2(self):
        button_pane = tk.Frame(self.windows, width=410, height=155, background="#4A1985")
        button_pane.place(x=742, y=221)
        
        button_dia = tk.Button(button_pane, text="Dia Grafico",
                               font=("Helvetica", 18),bg="#A580CA",
                               command= self.popDayGrafico)
        button_dia.place(x = 4, y= 4, width=200)
        
        buttonDay = tk.Button(button_pane, text="Agulhas do Dia",
                               font=("Helvetica", 18),bg="#A580CA",
                               command= self.popDayProducts)
        buttonDay.place(x=207, y=4, width=200)
        
        buttonMonth = tk.Button(button_pane, text="Total do Mês",
                               font=("Helvetica", 18),bg="#A580CA",
                               command= self.monthTotalPoP)
        buttonMonth.place(x=207, y= 54, width=200)    
        
        button_graficoPizza = tk.Button(button_pane, text="Grafico pizza",
                                        font=("Helvetica", 18),bg="#A580CA",
                                        command= self.graficoPizzaPoP)
        button_graficoPizza.place(x=4, y= 54, width=200)
        
        button_graficoMes = tk.Button(button_pane, text="Grafico do mês"
                                      ,font=("Helvetica", 18),
                                      bg="#A580CA",command= self.monthlyGraph)
        button_graficoMes.place(x= 4 , y= 104, width=200)
        
        button_comparaMes = tk.Button(button_pane, text="Comparar o Mês",
                                      font=("Helvetica", 18),bg="#A580CA",
                                      command= self.popComparacaoGrafico)
        button_comparaMes.place(x= 207 , y= 104, width=200)
        
                   
    def optionsFrame(self):
        optionPane = tk.Frame(self.windows, width=128, height=47,
                               background="#4A1985")
        optionPane.place(x=1040, y=20)
        
        self.storeDataMode = ttk.Combobox(master= optionPane, values=["Xlsx","MongoDB"],
                                        font=("Helvetica", 14),width= 8)
        self.storeDataMode.pack(padx= 2, pady= 2)
        self.storeDataMode.set("Xlsx")
              
    def buttonPainel(self):
        button_pane = tk.Frame(self.windows, width=334, height=114, background="#4A1985")
        button_pane.place(x=55, y=352)

        button_add = tk.Button(button_pane, text="Adicionar", font=("Helvetica", 18),
                               bg="#A580CA", command= self.addDayMongo)
        button_add.place(x=179, y= 58, width=149)

        button_skip_turn = tk.Button(button_pane, text="Pular turno",
                                     font=("Helvetica", 18),
                                     bg="#A580CA", command= self.passTurnFunc)
        button_skip_turn.place(x=6, y=58)

        button_add_more = tk.Button(button_pane, text="Adicionar + ",
                                    font=("Helvetica", 18),
                                    bg="#A580CA",command= self.popADD)
        button_add_more.place(x=179, y=7)
     
    def comboxSetor(self):
        self.combo_setor = ttk.Combobox(self.anchorPane, values=["Raschell",
                                        "Jacquard", "ketten"],
                                   font=("Helvetica", 14))
        self.combo_setor.place(x=21, y=92, width=87, height=25)
        self.combo_setor.set("Raschell")

    def comboTurno(self):
        self.combo_turno = ttk.Combobox(self.anchorPane, values=["TA", "TB", "TC"],
                                   font=("Helvetica", 14))
        self.combo_turno.place(x=142, y=92, width=87, height=25)
        self.combo_turno.set("TA")
                  
    def passTurnFunc(self):
        self.conts += 1
        self.clearLIstEntrys()
        if self.conts == 1:
            self.combo_turno.set("TB")
        else:
            self.combo_turno.set("TC")
            self.conts = 0
                     
    def finurasCheck(self, finura):
        asw = self.products.finuraCheck(finura)
        if not asw:
            self.popFinuras()
        else:
            return False
        
    def monthNotNumber(self, monthStr):
        try:
            month = int(monthStr)
            if type(month) != int or month >=13 or month == None or month == 0:
                return True
            else:
                return False
        except  ValueError :
            self.popMonth()
               
    def dayNotnumber(self, dayStr):
        try:
            day = int(dayStr)
            if type(day)!= int or day >=32 or day == "" or day == 0 or day == None :
                return True
            else:
                return False
        except  ValueError :
            self.popDay()
              
    def agulhaNotNumber(self, agulhaStr):
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
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Valor invalido",
                              font=("Helvetica", 27))
        messagebox.pack(padx= 40, pady= 40)   
        self.agulhaEntry.delete(0, END)
        #self.dayEntry.delete(0, END)
        #self.monthEntry.delete(0, END)
        self.listData = []
        self.contsAdd = 0
            
    def popAgulhaErrada(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Agulha invalida", 
                              font=("Helvetica", 27),
                              background="#A580CA")
        messagebox.pack(padx= 40, pady= 40)   
        self.agulhaEntry.delete(0, END)
        self.contsAdd = 0
               
    def popDay(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Dia errado",
                              font=("Helvetica", 27),
                              background="#A580CA")
        messagebox.pack(padx= 40, pady= 40)   
        self.dayEntry.delete(0, END)
        self.contsAdd = 0
    
    def popFinuras(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Finura Errada",
                              font=("Helvetica", 27),
                              background="#A580CA")
        messagebox.pack(padx=40, pady=40)   
        self.clearLIstEntrys()
        
    def popMonth(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(background= "#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Mês INVALIDO",
                              font=("Helvetica", 27),
                              background="#A580CA")
        messagebox.pack(padx=40, pady=40)   
        self.monthEntry.delete(0, END)
        self.contsAdd = 0
        
    def popMissClick(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(background="#A580CA")
        if self.combo_turno.get() == 'TA':
            messagebox = tk.Label(master= masterPoP,
                                text= "Erro faltam os turnos TB E TC",
                                wraplength=450,  # Wrap text after 450 pixels,
                                justify="center",
                                font=("Helvetica", 27),
                                width="500",
                                background="#A580CA")
            messagebox.pack(padx=40, pady=40)   
        elif self.combo_turno.get() == 'TB':
            messagebox = tk.Label(master= masterPoP,
                                text= "Erro falta o turno TC",
                                justify="center",
                                font=("Helvetica", 27),
                                background="#A580CA")
            messagebox.pack(padx=40, pady=40)
        
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Clicar em Adicionar mais ou Passar o turno")
                               
    def popExeception(self,finura="F14", month ="1", day=1, agulha = 1 ):
        self.GraficsOpen = False
        if self.monthNotNumber(month):
            self.popMonth()  
        elif self.dayNotnumber(day):
            self.popDay()      
        elif self.agulhaNotNumber(agulha):
            self.popAgulhaErrada()
        elif self.finurasCheck(finura):
            self.popFinuras()
        else: 
            False
     
    def popADD(self):
        self.popExeception( self.finuraEntry.get(),
                            month= self.monthEntry.get(),
                            day= self.dayEntry.get(),
                            agulha= self.agulhaEntry.get())
        if self.contsAdd > 1:
            self.popEraserError()          
        elif not self.finurasCheck(self.finuraEntry.get()) : 
            ask  = messagebox.askyesno("Confirmação", 
                                    message= "Confirmar os dados")
            self.askTrue(ask)
            return ask
     
    def askTrue(self, ask):
        try:
            self.contsAdd +=1
            if ask == True:
                dia = int(self.dayEntry.get())   
                mes = int(self.monthEntry.get())
                finura = self.finuraEntry.get()
                agulhas = int(self.agulhaEntry.get())
                turn = self.combo_turno.get()
                self.addFunc(turn, finura, agulhas)
                dataXlsx = {self.products.keyFinurasAppend(turn,
                                             finura.upper()): agulhas}
                self.products.addDayDataListXlsx(dia, turn, dataXlsx)
                self.clearLIstEntrys()
            else: 
                self.askNot()
                
        except ValueError:
            self.popValueError()
                  
    def askNot(self):
        self.finuraEntry.delete(0, END)
        self.agulhaEntry.delete(0, END)
        
    def clearLIstEntrys(self):
        self.listData = []
        self.finuraEntry.delete(0, END)
        self.agulhaEntry.delete(0, END)
        self.contsAdd = 0
        
    def dayPopButton(self):
        popDia = Tk()
        popDia.geometry("300x200")
        popDia.config(background="#4A1985") 
        messagebox = tk.Label(master= popDia, text= "Digite o dia:",
                            font=("Helvetica", 14), bg="#4A1985")
        messagebox.pack(padx= 2, pady= 20) 
        
        combo_setor = ttk.Combobox(popDia, values=["Raschell", "Jacquard", "ketten"],
                                   font=("Helvetica", 14), background= "#A580CA")
        combo_setor.place(x=105, y= 115, width=87, height=25)
        combo_setor.set("Setor")
        
        button_ok = tk.Button(popDia, text="Iniciar",font=("Helvetica", 18),
                                        bg="#A580CA",command= self.popDayGrafico)
        button_ok.place(x= 105 , y= 155, width= 88, height= 35)
        
        self.diaGraficoEntry1 = tk.Entry(master= popDia)     
        self.diaGraficoEntry1.pack(padx= 6, pady= 2)
         
    def popComparacaoGrafico(self):
        popComparacao = Tk()
        popComparacao.geometry("250x180")
        popComparacao.config(background="#9F5FFF")
   
        self.compSetor = ttk.Combobox(master= popComparacao, 
                                   values=["RASCHELL", "JACQUARD", "KETTEN"],
                                   font=("Helvetica", 14), background= "#9F5FFF")
        self.compSetor.place(x=10, y=30, width=140, height=25)
        self.compSetor.set("RASCHELL")
        
        messageboxMes1 = tk.Label(master= popComparacao, text= "Mês 1:",
                            font=("Helvetica", 18), bg="#9F5FFF")
        messageboxMes1.place(x=9, y=80)
        
        self.compMonthEntry1 = tk.Entry(master= popComparacao)     
        self.compMonthEntry1.place(x=87, y= 85, width="42", height="23")
        
        messageboxMes2 = tk.Label(master= popComparacao, text= "mês 2:",
                            font=("Helvetica", 18), bg="#9F5FFF")
        messageboxMes2.place(x=122, y=80)
        
        self.compMonthEntry2 = tk.Entry(master= popComparacao)     
        self.compMonthEntry2.place(x=198 , y= 85, width="42", height="23")
        
        buttonMes = tk.Button(popComparacao, text="Inciar",font=("Helvetica", 18),
                                        bg="#9F5FFF",command= self.popCompSelect)
        buttonMes.place(x= 10 , y= 140, width= 95, height= 25) 
        
        
    def monthTotalPoP(self):
        monthLyGraph = Tk()
        monthLyGraph.geometry("200x200")
        monthLyGraph.config(background="#9F5FFF")
        monthLyGraph.title("Grafico do mes")
        
        self.comboSetorMonth1 = ttk.Combobox(monthLyGraph, values=["RASCHELL", "JACQUARD", "KETTEN"],
                                   font=("Helvetica", 14), background= "#9F5FFF")
        self.comboSetorMonth1.place(x=10, y=30, width=140, height=25)
        self.comboSetorMonth1.set("RASCHELL")
        
        messagebox = tk.Label(master= monthLyGraph, text= "Mês:",
                            font=("Helvetica", 18), bg="#9F5FFF")
        messagebox.place(x=10, y=80)
        
        self.monthGraficEntry = tk.Entry(master= monthLyGraph)     
        self.monthGraficEntry.place(x=75, y= 85, width="42", height="23")
        
        button_ok = tk.Button(monthLyGraph, text="Iniciar",font=("Helvetica", 18),
                                        bg="#9F5FFF",command= self.monthTotalDisplay)
        button_ok.place(x= 10 , y= 140, width= 95, height= 25)
      
    def monthTotalDisplay(self):
        valueY = 58
        dataMonthSum = []
        data = []
        ask = self.monthNotNumber(self.monthGraficEntry.get())
        if ask:
            self.popMonth()
        elif not ask == None:
            data = self.products.dataGraphMonth(self.comboSetorMonth1.get(),
                                            self.monthGraficEntry.get())
            dataMonthSum = self.products.monthTotalSum(data)[0]
            monthLyGraph = Tk()
            monthLyGraph.geometry("900x400")
            monthLyGraph.config(background="#A580CA")
            
            messagebox = tk.Label(master= monthLyGraph, text= "Mês:",
                                font=("Helvetica", 25), bg="#A580CA")
            messagebox.place(x=17, y=10)
            
            messageboxMonth = tk.Label(master= monthLyGraph, 
                                    text= f"{self.monthGraficEntry.get()}",
                                font=("Helvetica", 25), bg="#A580CA")
            messageboxMonth.place(x=95, y=10)
            
            messageboxSetor = tk.Label(master= monthLyGraph, 
                                    text= f"{self.comboSetorMonth1.get()}",
                                font=("Helvetica", 25), bg="#A580CA")
            messageboxSetor.place(x=200, y=10)
            
            messageboxTotalTop = tk.Label(master= monthLyGraph, text= "TOTAL:",
                                        font=("Helvetica", 30), bg="#A580CA")
            messageboxTotalTop.place(x= 15 , y= 60)
            
            for key, values in dataMonthSum.items():
                valueY += 53
                messageboxTotal = tk.Label(master= monthLyGraph, text= f"{key} : {values}",
                                        font=("Helvetica", 30), bg="#A580CA")
                messageboxTotal.place(x= 15, y=valueY)
                #adicionar por dia divisao
            
        
    def monthlyGraph(self):
        monthLyGraph = Tk()
        monthLyGraph.geometry("200x200")
        monthLyGraph.config(background="#9F5FFF")
        
        self.comboSetorAllMonth = ttk.Combobox(monthLyGraph,
                                   values=["RASCHELL", "JACQUARD", "KETTEN"],
                                   font=("Helvetica", 14), background= "#9F5FFF")
        self.comboSetorAllMonth.place(x=10, y=30, width=140, height=25)
        self.comboSetorAllMonth.set("RASCHELL")
        
        messagebox = tk.Label(master= monthLyGraph, text= "Mês:",
                            font=("Helvetica", 18), bg="#9F5FFF")
        messagebox.place(x=10, y=80)
        
        self.allMonthGraficEntry = tk.Entry(master= monthLyGraph)     
        self.allMonthGraficEntry.place(x=75, y= 85, width="42", height="23")
        
        button_ok = tk.Button(monthLyGraph, text="Iniciar",font=("Helvetica", 18),
                                        bg="#9F5FFF",command= self.popFinurasSelectMonth)
        button_ok.place(x= 10 , y= 160, width= 95, height= 25)
    
    def popFinurasSelectMonth(self):
        ask = self.monthNotNumber(self.allMonthGraficEntry.get())
        if ask:
            self.popMonth()
        elif not ask == None:
            monthLyGraph = Tk()
            monthLyGraph.geometry("200x200")
            monthLyGraph.config(background="#9F5FFF")

            messagebox = tk.Label(master= monthLyGraph, text= "Finura:",
                                font=("Helvetica", 18), bg="#9F5FFF")
            messagebox.place(x=10, y=60)
            
            if self.comboSetorAllMonth.get() == "RASCHELL":
                self.comboFinurasAllMonth = ttk.Combobox(monthLyGraph,
                                            values=["3975", "4575","4475", "4565"],
                                            font=("Helvetica", 14), background= "#9F5FFF")
                self.comboFinurasAllMonth.place(x=10, y=100, width=140, height=25)
                self.comboFinurasAllMonth.set("3975")
            elif self.comboSetorAllMonth.get() == "JACQUARD":
                self.comboFinurasAllMonth = ttk.Combobox(monthLyGraph,
                                            values=["4496", "2760"],
                                            font=("Helvetica", 14), background= "#9F5FFF")
                self.comboFinurasAllMonth.place(x=10, y=100, width=140, height=25)
                self.comboFinurasAllMonth.set("4496")
            else:
                self.comboFinurasAllMonth = ttk.Combobox(monthLyGraph,
                                            values=["2760"],
                                            font=("Helvetica", 14), background= "#9F5FFF")
                self.comboFinurasAllMonth.place(x=10, y=100, width=140, height=25)
                self.comboFinurasAllMonth.set("2760")
            
            button_ok = tk.Button(monthLyGraph, text="Iniciar",font=("Helvetica", 18),
                                            bg="#9F5FFF",command= self.allMonthGraphic)
            button_ok.place(x= 10 , y= 150, width= 95, height= 25)   
        
        
    def monthGraphicData(self):
        self.products.clearList()
        self.comboSetorMonth =""
        self.monthGraficEntry = ""
        return self.products.dataGraphAllMonthTotal(self.comboSetorAllMonth.get(),
                                        self.allMonthGraficEntry.get())
    
    def monthGraphicPoP(self):
        self.products.clearList()
        graphicMonth = Tk()
        graphicMonth.geometry("200x200")
        graphicMonth.config(background="#9F5FFF")
        valueY = 2
        data = self.monthGraphicData()
        
        messageboxTotalTop = tk.Label(master= graphicMonth, text= "TOTAL:",
                                    font=("Helvetica", 30), bg="#A580CA")
        messageboxTotalTop.place(x=30, y= valueY)
        for key, values in data.items():
            valueY += 53
            messageboxTotal = tk.Label(master= graphicMonth, text= f"{key} : {values}",
                                    font=("Helvetica", 30), bg="#A580CA")
            messageboxTotal.place(x=30, y=valueY)
        
        
    def addFunc(self, turn, finura , agulha):
        dataList = [{finura : agulha}]
        list(map(lambda data: self.listData.append(data), dataList))
        self.products.addAgulhasinDictList(turn, self.listData)
        self.products.sumList(finura, agulha, self.storeDataMode.get())
           
    def addDayMongo(self):
        if self.combo_turno.get() != 'TC':
            self.popMissClick()
        else:
            if self.storeDataMode.get() == "MongoDB":
                self.products.sumDay()
                setorStr = self.combo_setor.get()
                brokenDay = self.products.addDay(str(self.monthEntry.get()),
                                                int(self.dayEntry.get()),
                                                setorStr.upper())
                self.products.productService.addDayAgulhaBrokeMongoDB(brokenDay)
                self.clearLIstEntrys()
                self.products.clearList()
                self.combo_turno.set("TA")
                self.popDiaAdd()
            else : 
                self.products.sumDay()
                setorStr = self.combo_setor.get()
                self.products.addDayXlxs(str(self.monthEntry.get()),
                                        int(self.dayEntry.get()), setorStr.upper())
                self.products.clearList()
                self.combo_turno.set("TA")
                self.popDiaAdd()
                
    def popDiaAdd(self):
        diaPOP= Tk()
        diaPOP.geometry("300x300")
        diaPOP.config(background="#871188")
        
        messageboxTotalTop = tk.Label(master= diaPOP, text= "Dia Adicionado",
                                    font=("Helvetica", 30), bg="#871188", width= 12)
        messageboxTotalTop.place(x= 7, y = 120)
                                                   
    #START MATPLOT INTERATION
    def closedPlt(self):
        # Cancel the scheduled after() event if it exists
        if self.close_after_id is not None:
            self.plot_window.after_cancel(self.close_after_id)
            self.close_after_id = None
        # Destroy the Tkinter window if it exists
        if self.plot_window and tk.Toplevel.winfo_exists(self.plot_window):
            self.plot_window.destroy()
            self.plot_window = None
    
    #triger of popDayResult 
    def popDayProducts(self):
        graphicDaySetor = Tk()
        graphicDaySetor.geometry("200x200")
        graphicDaySetor.config(background="#9F5FFF")
        
        messagebox = tk.Label(master= graphicDaySetor, text= "Selecione o Setor:",
                            font=("Helvetica", 14), bg="#9F5FFF")
        messagebox.place(x= 18, y= 20)
        
        self.combo_setorDay = ttk.Combobox(master= graphicDaySetor,
                                    values=["RASCHELL", "JACQUARD", "KETTEN"],
                                   font=("Helvetica", 14), background= "#9F5FFF")
        self.combo_setorDay.place(x= 20, y= 75, width=140, height=25)
        self.combo_setorDay.set("RASCHELL")
        
        buttonOk = tk.Button(graphicDaySetor, text="OK",
                                    font=("Helvetica", 14),
                                    command= self.popDayProductsSetor)
        buttonOk.place(x=20, y=120)
    
    #triger for popDayProducs       
    def popDayProductsSetor(self):
        try:
            ask = self.popExeception(month= self.monthEntry.get(),
                                     day = self.dayEntry.get())
            if not ask:                           
                day = int(self.dayEntry.get())
                dictData= self.products.popDayProducts(self.monthEntry.get(), 
                                                    self.combo_setorDay.get(), day,
                                                    self.storeDataMode.get())
                self.popDayResult(dictData)
        except AttributeError:
            self.popDay()
               
    #print result dynamics with label in frame                            
    def popDayResult(self, data):
        valueY = 2
        graphicDay = Tk()
        graphicDay.geometry("900x400")
        graphicDay.config(background="#A580CA")
        
        try:
            #TA
            dataSlice = data[0]
            messageboxTotalTATOP = tk.Label(master= graphicDay, text= "TA:",
                                        font=("Helvetica", 30), bg="#A580CA")
            messageboxTotalTATOP.place(x=10, y =valueY)
            for key, values in dataSlice.items():
                valueY += 53
                messageboxTA = tk.Label(master= graphicDay, text= f"{key} : {values}",
                                        font=("Helvetica", 30), bg="#A580CA")
                messageboxTA.place(x=10, y =valueY)
            #TB
            dataSlice = data[1]
            valueY = 2
            messageboxTotalTBTOP = tk.Label(master= graphicDay, text= "TB:",
                                        font=("Helvetica", 30), bg="#A580CA")
            messageboxTotalTBTOP.place(x= 185, y = valueY)
            for key, values in dataSlice.items():
                valueY += 53
                messageboxTB = tk.Label(master= graphicDay, text= f"{key} : {values}",
                                        font=("Helvetica", 30), bg="#A580CA")
                messageboxTB.place(x=185, y=valueY)
            #TC
            dataSlice = data[2]
            valueY = 2
            messageboxTotalTCTOP = tk.Label(master= graphicDay, text= "TC:",
                                        font=("Helvetica", 30), bg="#A580CA")
            messageboxTotalTCTOP.place(x=395, y=valueY)
            for key, values in dataSlice.items():
                valueY += 53
                messageboxTC = tk.Label(master= graphicDay, text= f"{key} : {values}",
                                        font=("Helvetica", 30), bg="#A580CA")
                messageboxTC.place(x=395, y=valueY)
            #TOTAL      
            dataSlice = data[3]
            valueY = 2
            messageboxTotalTop = tk.Label(master= graphicDay, text= "TOTAL:",
                                        font=("Helvetica", 30), bg="#A580CA")
            messageboxTotalTop.place(x=650, y= valueY)
            for key, values in dataSlice.items():
                valueY += 53
                messageboxTotal = tk.Label(master= graphicDay, text= f"{key} : {values}",
                                        font=("Helvetica", 30), bg="#A580CA")
                messageboxTotal.place(x=650, y=valueY)
        except TypeError:
            self.popValueError()                       
                            
    def graficoPizzaPoP(self):
        pizzaGraf = Tk()
        pizzaGraf.title("Grafico pizza")
        pizzaGraf.geometry("240x220")
        pizzaGraf.config(background="#9F5FFF")
        
        self.comboSetorPizza = ttk.Combobox(pizzaGraf, 
                                   values=["RASCHELL", "JACQUARD", "KETTEN"],
                                   font=("Helvetica", 14), background= "#9F5FFF")
        self.comboSetorPizza.place(x=10, y=30, width=140, height=25)
        self.comboSetorPizza.set("RASCHELL")
        
        messagebox = tk.Label(master= pizzaGraf, text= "Mês:",
                            font=("Helvetica", 18), bg="#9F5FFF")
        messagebox.place(x=10, y=80)
        
        self.pizzaGraficEntryMonth = tk.Entry(master= pizzaGraf)     
        self.pizzaGraficEntryMonth.place(x=65, y= 85, width="42", height="23")
        
        messageboxDia = tk.Label(master= pizzaGraf, text= "Dia:",
                            font=("Helvetica", 18), bg="#9F5FFF")
        messageboxDia.place(x=114, y=80)
        
        self.pizzaGraficEntryDay = tk.Entry(master= pizzaGraf)     
        self.pizzaGraficEntryDay.place(x=163 , y= 85, width="42", height="23")
        
        buttonMes = tk.Button(pizzaGraf, text="Mês",font=("Helvetica", 18),
                                        bg="#9F5FFF",command= self.pizzaDisplayMonth)
        buttonMes.place(x= 10 , y= 140, width= 95, height= 25) 
        
        buttonDia = tk.Button(pizzaGraf, text="Dia",font=("Helvetica", 18),
                                        bg="#9F5FFF",command= self.pizzaDisplayDay)
        buttonDia.place(x= 110 , y= 140, width= 95, height= 25)              
    
    def popDayGrafico(self):
        valueAgulha = []
        finuraKey = []
        agulhaTotalRed = []
        varStack = []
        varItemsStack = []
        try:
            ask = self.popExeception(day= self.dayEntry.get(),
                    month=self.monthEntry.get())
            if not ask:
                self.GraficsOpen = True
                self.day = int(self.dayEntry.get())
                self.month = self.monthEntry.get()
        except ValueError:
            return self.popDay()
        if self.GraficsOpen:
            for setor in range(3):    
                dictData = self.products.popDayProducts(self.month,
                        Enumstoday.getEnumsSetorNames(self, setor), self.day,
                        self.storeDataMode.get())
                varStack.append(dictData[-1]) 
                #add dict in list of value
                for dictList in dictData:
                    for keys , value in dictList.items():
                        valueAgulha.append(value)
                        finuraKey.append(keys)
                        if dictList != varStack[0]:
                            agulhaTotalRed.append(0)       
                #Paint red for total
                for totalDicts in varStack:
                    varItemsStack.append(totalDicts)
                    for totalKeys, totalValues in totalDicts.items():
                        agulhaTotalRed.append(totalValues)
                #add space
                for space in range(3):
                    valueAgulha.append(0)
                    finuraKey.append("")
                    agulhaTotalRed.append(0)
                varStack = []
            # Check if there's already an open window, close it
            if self.plot_window and tk.Toplevel.winfo_exists(self.plot_window):
                self.plot_window.destroy()
            # Create a new top-level window
            self.plot_window = tk.Toplevel()  # Use Toplevel instead of Tk
            self.plot_window.title("PoP Day Graphics Bar")
            self.plot_window.config(background="#A580CA")
            self.plot_window.geometry("1000x500")
            try: 
                categories = np.arange(1, (len(valueAgulha)+1))
                fig, ax = plt.subplots(figsize=(50, 6))

                x = np.arange(len(categories))
                plt.bar(x , valueAgulha,  label='Value 1', color='b', align='center')
                ax.set_xlabel('Agulhas')
                ax.set_title('Agulhas quebradas')
                plt.xticks(x, labels= finuraKey)  
                plt.xlim(-0.5, len(categories) - 0.5)
                plt.ylim(0, 130) 
                plt.yticks(np.arange(0, 131, 5))
                
                #add Red color in total
                plt.bar(x , agulhaTotalRed,  label='Value 1', color='r', align='center')
                plt.xlim(-0.5, len(categories) - 0.5)
                
                #Labels setors
                ax.text(3, 0+ 40.0, f'("Raschell")', ha='center', color='red', fontsize=21)
                ax.text(11, 0+ 40.0, f'("Jacquard")', ha='center', color='red', fontsize=21)
                ax.text(18, 0+ 40.0, f'("Ketten")', ha='center', color='red', fontsize=21)
                
                # Embed the plot in the Tkinter window
                canvas = FigureCanvasTkAgg(fig, master=self.plot_window)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
                # Schedule the window to close after 15 seconds
                self.close_after_id = self.plot_window.after(150000, self.closedPlt)
                self.plot_window.protocol("WM_DELETE_WINDOW", self.closedPlt)
                self.plot_window.mainloop()
            except ValueError:
                self.popValueError()          
                                        
    def allMonthGraphic(self):
        self.products.clearList()
        self.comboSetorMonth =""
        self.monthGraficEntry = ""
        dictData = self.products.dataGraphAllMonth(self.comboSetorAllMonth.get(),
                                        self.allMonthGraficEntry.get(),
                                        self.comboFinurasAllMonth.get())
        valueAgulha = []
        #add dict in list of value
        for dictSlice in dictData:
            for dictList in dictSlice:
                for keys , value in dictList.items():
                    valueAgulha.append(value)    
                    
        # Check if there's already an open window, close it
        if self.plot_window and tk.Toplevel.winfo_exists(self.plot_window):
            self.plot_window.destroy()
        # Create a new top-level window
        self.plot_window = tk.Toplevel()  # Use Toplevel instead of Tk
        self.plot_window.title("PoP Day Graphics Bar")
        self.plot_window.config(background="#A580CA")
        self.plot_window.geometry("1000x500")
        try:  
            categories = np.arange(1, (len(valueAgulha)+1))
            fig, ax = plt.subplots(figsize=(50, 6))
            
            x = np.arange(1, (len(categories)+1))
            plt.bar(x, valueAgulha,  label='Value 1', color='b', align='center')
            ax.set_xlabel('Dias')
            ax.set_ylabel('Agulhas')
            ax.set_title('Agulhas quebradas')  
            plt.xlim(-0.2, (len(categories)+1) - 0.1)
            plt.ylim(0, 130) 
            plt.xticks(x)
            plt.yticks(np.arange(0, 131, 5))
            
            #add Red color in hight total in month beta
            #plt.bar(x , agulhaTotalRed,  label='Value 1', color='r', align='center')
            #plt.xlim(-0.5, len(categories) - 0.5)
           
            #Labels setors 
            ax.text(18, 20+ 40.0,
            f"{self.comboSetorAllMonth.get()} Codigo: {self.comboFinurasAllMonth.get()}"
                                               ,ha='center', color='red', fontsize=21)
            
            # Embed the plot in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
            # Schedule the window to close after 15 seconds
            self.close_after_id = self.plot_window.after(150000, self.closedPlt)
            self.plot_window.protocol("WM_DELETE_WINDOW", self.closedPlt)
            self.plot_window.mainloop()
        except ValueError:
            self.popValueError()
                    
    def pizzaDisplayMonth(self):
        nameList = []
        valueList = []
        explodeList = []
        askMonth = self.monthNotNumber(self.pizzaGraficEntryMonth.get())
        if askMonth:
            self.popMonth()
        elif not askMonth == None:
            data = self.products.pizzaDataMonth(self.comboSetorPizza.get(),
                                                self.pizzaGraficEntryMonth.get())
            for lists in data:
                for keys , values in lists.items():
                    nameList.append((keys))
                    valueList.append(values)
                    explodeList.append((0))
            labels = nameList
            explode = explodeList  
            sizes = valueList
            colorsLen = len(nameList)
            colorList = ['#A580CA','#FF9999', '#66b3ff','#99ff99',"#A77EB0"
                            "#B89BCC", "#C8A2D6", "#FF99CC", '#FF66B2']
            colors = list(filter(lambda x: colorsLen <= len(colorList), colorList ))
                
            # Create a Figure and a Pie Chart
            root = tk.Tk()
            root.title("Pie Chart Example")
            fig = Figure(figsize=(10, 10), dpi=100)
            ax = fig.add_subplot(111)
            ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%10.1f%%',  startangle=140 )
            ax.axis('equal')
            ax.set_title('Pizza grafico do mês', pad= 25.0)
            
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def pizzaDisplayDay(self):
        nameList = []
        valueList = []
        explodeList = []
        askMonth = self.monthNotNumber(self.pizzaGraficEntryMonth.get())
        askDay = self.dayNotnumber(self.pizzaGraficEntryDay.get())
        if askMonth:
            self.popMonth()
        elif askDay:
            self.popDay()
        elif not askMonth == None and not askDay == None:
            data = self.products.pizzaDataDay(self.pizzaGraficEntryMonth.get(),
                                            self.comboSetorPizza.get(),
                                            int(self.pizzaGraficEntryDay.get()),
                                            self.storeDataMode.get())
            for lists in data:
                for keys , values in lists.items():
                    nameList.append((keys))
                    valueList.append(values)
                    explodeList.append((0))
            labels = nameList
            explode = explodeList  
            sizes = valueList
            colorsLen = len(nameList)
            colorList = ['#A580CA','#FF9999', '#66b3ff','#99ff99',"#A77EB0", "#9B5BA0",
                        "#B89BCC", "#C8A2D6", "#FF99CC", '#FF66B2', "#A66FC4 ", "#B39CDE"]
            colors = list(filter(lambda x: colorsLen <= len(colorList), colorList ))
            
        # Create a Figure and a Pie Chart
            root = tk.Tk()
            root.title("Pie Chart Example")
            fig = Figure(figsize=(10, 10), dpi=100)
            ax = fig.add_subplot(111)
            ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%',  startangle=140 )
            ax.axis('equal')
            ax.set_title('Quebra do Dia', pad= 25.0)
        
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def popCompSelect(self):
        month1 = self.monthNotNumber(self.compMonthEntry1.get())
        month2 = self.monthNotNumber(self.compMonthEntry2.get())
        if not month1 and not month2 and not month1 == None and not month2 == None:
            popCompRoot = Tk()
            popCompRoot.geometry("200x200")
            popCompRoot.config(background="#9F5FFF")
            popCompRoot.title("Finuras select")

            messagebox = tk.Label(master= popCompRoot, text= "Finura:",
                                font=("Helvetica", 18), bg="#9F5FFF")
            messagebox.place(x=10, y=60)
            
            if self.compSetor.get() == "RASCHELL":
                self.comboCompFinuras = ttk.Combobox(popCompRoot,
                                            values=["3975", "4575","4475", "4565"],
                                            font=("Helvetica", 14), background= "#9F5FFF")
                self.comboCompFinuras.place(x=10, y=100, width=140, height=25)
                self.comboCompFinuras.set("3975")
            elif self.compSetor.get() == "JACQUARD":
                self.comboCompFinuras = ttk.Combobox(popCompRoot,
                                            values=["4496", "2760"],
                                            font=("Helvetica", 14), background= "#9F5FFF")
                self.comboCompFinuras.place(x=10, y=100, width=140, height=25)
                self.comboCompFinuras.set("4496")
            else:
                self.comboCompFinuras = ttk.Combobox(popCompRoot,
                                            values=["2760"],
                                            font=("Helvetica", 14), background= "#9F5FFF")
                self.comboCompFinuras.place(x=10, y=100, width=140, height=25)
                self.comboCompFinuras.set("2760")
            
            button_ok = tk.Button(popCompRoot, text="Iniciar",font=("Helvetica", 18),
                                            bg="#9F5FFF",command= self.popCompDisplay)
            button_ok.place(x= 10 , y= 150, width= 95, height= 25)   
        
    def popCompDisplay(self):
        nameList = []
        valueList = []
        explodeList = []
        data1 = self.products.pizzaDataComp(self.compMonthEntry1.get(),
                                            self.compSetor.get(),
                                            self.comboCompFinuras.get())
        
        data2 = self.products.pizzaDataComp(self.compMonthEntry2.get(),
                                            self.compSetor.get(),
                                            self.comboCompFinuras.get())
        
        #add dict list in list
        valueList1 = list(data1[0][0].values())
        valueList2 = list(data2[0][0].values())
        nameList.append((data1[1]))
        nameList.append((data2[1]))
        valueList.append(valueList1[0])
        valueList.append(valueList2[0])
       
        labels = nameList
        sizes = valueList
        explode = [0, 0] 
        colorsLen = len(nameList)
        colorList = ['#A580CA','#FF9999', '#66b3ff','#99ff99',"#A77EB0"
                     "#B89BCC", "#C8A2D6", "#FF99CC", '#FF66B2']
        colors = list(filter(lambda x: colorsLen <= len(colorList), colorList ))
        
       # Create a Figure and a Pie Chart
        root = tk.Tk()
        root.title("Pie Chart Example")
        fig = Figure(figsize=(10, 10), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%10.1f%%',  startangle=140, )
        ax.axis('equal')
        ax.set_title('Pizza grafico do mês', pad= 25.0)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    