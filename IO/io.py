import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from products.Products import Products
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from functools import cache


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
        self.plot_window = None
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

        #self.dayEntry = tk.Entry(self.anchorPane, font=("Helvetica", 14))
        #self.dayEntry.place(x=120, y=144, width=81, height=26)

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
        button_pane = tk.Frame(self.windows, width=410, height=104, background="#4A1985")
        button_pane.place(x=742, y=270)
        button_dia = tk.Button(button_pane, text="Agulhas do Dia",
                               font=("Helvetica", 18),bg="#A580CA",
                               command= self.popDayGrafico)
        button_dia.place(x = 4, y= 4, width=200)
        
        button_graficoPizza = tk.Button(button_pane, text="Grafico pizza",
                                        font=("Helvetica", 18),bg="#A580CA",
                                        command= self.popComparacaoGrafico)
        button_graficoPizza.place(x= 207 , y= 4, width=200)
        
        button_graficoMes = tk.Button(button_pane, text="Grafico do mês"
                                      ,font=("Helvetica", 18),
                                      bg="#A580CA",command= self.monthlyGraph)
        button_graficoMes.place(x= 207 , y= 54, width=200)
        
        button_comparaMes = tk.Button(button_pane, text="Comparar o Mês",
                                      font=("Helvetica", 18),bg="#A580CA",
                                      command= self.popComparacaoGrafico)
        button_comparaMes.place(x= 4 , y= 54, width=200)
              
    
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
            if type(day) != int or day >=32 or day == "" or day == 0 or day == None:
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
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Valor invalido",
                              font=("Helvetica", 27))
        messagebox.pack(padx= 40, pady= 40)   
        self.agulhaEntry.delete(0, END)
        self.dayEntry.delete(0, END)
        self.monthEntry.delete(0, END)
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
                self.addFunc(turn, finura, agulhas)
                self.clearLIstEntrys()
        except ValueError:
            self.popValueError()
                  
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
        popComparacao.geometry("300x200")
        popComparacao.config(background="#4A1985")
        messagebox = tk.Label(master= popComparacao, text= "Digite os Mês:",
                            font=("Helvetica", 14), bg="#4A1985")
        messagebox.pack(padx= 2, pady= 20) 
        
        comboSetor = ttk.Combobox(popComparacao, values=["Raschell", "Jacquard", "ketten"],
                                   font=("Helvetica", 14), background= "#A580CA")
        comboSetor.place(x=105, y= 52, width=87, height=25)
        comboSetor.set("Setor")
        
        self.comparacaoMonth1 = tk.Entry(master= popComparacao)     
        self.comparacaoMonth1.pack(padx= 6, pady= 20)
        
        self.comparacaoMonth2 = tk.Entry(master= popComparacao)     
        self.comparacaoMonth2.pack(padx= 6, pady= 1)
        
        button_ok = tk.Button(popComparacao, text="Iniciar",font=("Helvetica", 18),
                                        bg="#A580CA",command= "beta")
        button_ok.place(x= 105 , y= 155, width= 88, height= 35)
        
    def monthlyGraph(self):
        monthLyGraph = Tk()
        monthLyGraph.geometry("900x400")
        monthLyGraph.config(background="#4A1985")
        
        combo_setor = ttk.Combobox(monthLyGraph, values=["Raschell", "Jacquard", "ketten"],
                                   font=("Helvetica", 14), background= "#A580CA")
        combo_setor.place(x=2, y= 10, width=87, height=25)
        combo_setor.set("Setor")
        
        messagebox = tk.Label(master= monthLyGraph, text= "Mês:",
                            font=("Helvetica", 14), bg="#4A1985")
        messagebox.place(x = 94, y = 7)
        
        self.monthGraficEntry = tk.Entry(master= monthLyGraph)     
        self.monthGraficEntry.place(x= 147, y =10, width="42", height="23")
        
        button_ok = tk.Button(monthLyGraph, text="Iniciar",font=("Helvetica", 18),
                                        bg="#A580CA",command= "beta")
        button_ok.place(x= 200 , y= 10, width= 88, height= 25)
    
    def addFunc(self, turn, finura , agulha):
        dataList = [{finura : agulha}]
        list(map(lambda data: self.listData.append(data), dataList))
        self.products.addAgulhasinDictList(turn, finura, self.listData)
        self.products.sumList(finura, agulha)
           
    def addDayMongo(self):
        if self.combo_turno.get() != 'TC':
            self.popMissClick()
        else:
            self.products.sumDay()
            brokenDay = self.products.addDay(str(self.monthEntry.get()),
                                             int(self.dayEntry.get()),
                                             self.combo_setor.get())
            print(self.products.sumDay())
            print(brokenDay)
            self.products.productService.addDayAgulhaBrokeMongoDB(brokenDay)
            self.clearLIstEntrys()
            self.combo_turno.set("TA")
                             
    #START MATPLOT INTERATION
    @cache
    def popDayGrafico(self):
        # Check if there's already an open window, close it
        if self.plot_window and tk.Toplevel.winfo_exists(self.plot_window):
            self.plot_window.destroy()

        # Create a new top-level window
        self.plot_window = tk.Toplevel()  # Use Toplevel instead of Tk
        self.plot_window.title("PoP Day Graphics")
        self.plot_window.config(background="#A580CA")
        self.plot_window.geometry("1000x500")

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(12, 6)) 

        # Generate data for the bar graph
        x = self.products.monthGraphics(7)
        y = self.products.monthGraphics(6)

        # Plot the bar graph
        ax.bar(x, y)
        ax.set_xlabel('Dia')
        ax.set_ylabel('Agulhas')
        ax.set_title('Agulhas quebradas')
        plt.xticks(rotation=45)
        
        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Schedule the window to close after 15 seconds
        self.close_after_id = self.plot_window.after(15000, self.closedPlt)
        self.plot_window.protocol("WM_DELETE_WINDOW", self.closedPlt)
        self.plot_window.mainloop()
        
    def closedPlt(self):
        # Cancel the scheduled after() event if it exists
        if self.close_after_id is not None:
            self.plot_window.after_cancel(self.close_after_id)
            self.close_after_id = None
        # Destroy the Tkinter window if it exists
        if self.plot_window and tk.Toplevel.winfo_exists(self.plot_window):
            self.plot_window.destroy()
            self.plot_window = None
                                                  
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    