from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsFinuras import EnumsFinuras
from typing import Dict
import collections, functools, operator, random
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook

RASCHELLIST = [3975, 4575, 4475, 4565]
JAQUARDLIST = [4496, 2760]
KETEN = [2660]

class Products():
    def __init__(self) :
        self.monthTotalDict = {}
        self.productService = ProductsService()
        self.enumsMonthDays = EnumsMonthDays()
        self.enumsFinuras = EnumsFinuras()
        self.listNeedlesBrokenDayTA = [] 
        self.listNeedlesBrokenDayTB = []  
        self.listNeedlesBrokenDayTC = [] 
        self.listSumNedlleDict = []
        self.NEDLLESCODESUM = RASCHELLIST + JAQUARDLIST + KETEN
        self.year = "2024"
        self.listSumDayResult = []
        self.listOfGetDocumentsDay = []
        self.listSumMonthResult = []
        self.listMonthTotalResult = []
        self.listDayXlsx = []
        self.dayTurnData = []
        self.rowDataListDay = []
        self.dictDataXlsx = {}
        self.conts = 0
       
    def monthTotalSum(self, data): 
        totalSum = collections.defaultdict(int)
        for nedlleList in data:
            for key, value in nedlleList.items():
                totalSum[key] += value
        [{'{}'.format(key): value}for key, value in totalSum.items()]
        self.listSumMonthResult.append(dict(totalSum))
        return self.listSumMonthResult
            
    def addDayMongoDB(self, setor):
        dayMongo = self.addDay( setor)
        return dayMongo
  
    def addDay(self, month, day, setor)->Dict:
        dictDay= {self.year: month, setor : day, "AGULHAS":
                                    {"TA": self.listNeedlesBrokenDayTA,
                                     "TB": self.listNeedlesBrokenDayTB, 
                                     "TC": self.listNeedlesBrokenDayTC,
                                     "TOTAL": self.listSumDayResult}}
        return dictDay
             
    def convertFinurasInCodeBar(self, finuras, agulhas):
        finurasDict = {finuras: agulhas}
        return finurasDict
        
    def addAgulhasinDictList(self, turno, agulhasData ):
        match(turno):
            case "TA":
                self.listNeedlesBrokenDayTA.append(agulhasData)
                return self.listNeedlesBrokenDayTA
            case "TB":
                self.listNeedlesBrokenDayTB.append(agulhasData)
                return self.listNeedlesBrokenDayTB
            case "TC":
                self.listNeedlesBrokenDayTC.append(agulhasData)
                return self.listNeedlesBrokenDayTC
            case _:
                return "TURN ERROR"
    def clearList(self):
        self.listNeedlesBrokenDayTA = []
        self.listNeedlesBrokenDayTB = []
        self.listNeedlesBrokenDayTC = []
        self.listSumNedlleDict = []
        self.listSumDayResult = []
        self.listOfGetDocumentsDay = []
        self.listSumMonthResult = []
        self.listOfGetDocumentsDay = []
        self.listMonthTotalResult = []
            
    def finuraCheck(self, finuras):
        return self.enumsFinuras.checkFinurasEnums(finuras)
    
    def sumDay(self):
        totalSum = collections.defaultdict(int)
        for nedlleList in self.listSumNedlleDict:
            for key, value in nedlleList.items():
                totalSum[key] += value
        self.listSumNedlleDict = [{'{}'.format(key): value}
                                for key, value in totalSum.items()]
        self.listSumDayResult.append(dict(totalSum))
        return self.listSumDayResult
    
    #convert code and nedlle in dict list
    def sumList(self, finura, agulha):
        finuraCode = self.enumsFinuras.finurasCodeReturn(finura) 
        result_dict = {finuraCode: agulha}
        self.listSumNedlleDict.append(result_dict)
        return self.listSumNedlleDict
   
    def randImage(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = f"IO\image\ess{randInt}.png"
        return path
    
    def addAgulhasDayMongo(self, dict : dict) ->Dict:
        self.productService.addDayAgulhaBrokeMongoDB(dict)
                  
    def selectMonthgrafics(self, month):
        monthDays = self.enumsMonthDays.colectMonths(month)
        return monthDays
     
    def monthGraphics(self, month):
        monthResult = self.enumsMonthDays.colectMonths(month)
        return monthResult
    
    def getDocumentFind(self, name):
        document = self.productService.getDocumentFind(name)
        return document
      
    def popDayProducts(self, month, setor, day):
        self.clearList()
        #TA
        dictVar = {}
        try:
            document = self.getDocumentFind({"2024": month, f"{setor}": day})
            agulhas = document.get('AGULHAS', {})
            ta = agulhas.get('TA', [])
            ta_dicts = [{key: value} for sublist in ta for item in sublist for key, value in item.items()]
            for intens in ta_dicts:
                dictVar.update(intens)
            self.listOfGetDocumentsDay.append(dictVar)    
            #TB
            dictVar = {}
            tb = agulhas.get('TB', [])
            tb_dicts = [{key: value} for sublist in tb for item in sublist for key, value in item.items()]
            list(map(lambda intens: dictVar.update(intens), tb_dicts))
            self.listOfGetDocumentsDay.append(dictVar)     
            #TC
            dictVar = {}
            tc = agulhas.get('TC', [])
            tc_dicts = [{key: value} for sublist in tc for item in sublist for key, value in item.items()]
            list(map(lambda intens: dictVar.update(intens), tc_dicts))
            self.listOfGetDocumentsDay.append(dictVar)  
            #TOTAL
            dictVar = {}
            total = agulhas.get('TOTAL', [])
            total_dicts = [{key: value} for d in total for key, value in d.items()]
            list(map(lambda intens: dictVar.update(intens), total_dicts))
            self.listOfGetDocumentsDay.append(dictVar)   
            return self.listOfGetDocumentsDay
        except AttributeError:
            self.listOfGetDocumentsDay.append({"Nao teve quebra": 0})
            return self.listOfGetDocumentsDay
        
    def dataGraphMonth(self, setor, month):
        self.clearList()
        mes = self.enumsMonthDays.colectMonths(int(month))
        for days in range(mes):
            try:
                document = self.getDocumentFind({"2024": f"{month}", f"{setor}": days})
                agulhas = document.get('AGULHAS', {})
                
                dictVar = {}
                total = agulhas.get('TOTAL', [])
                total_dicts = [{key: value} for d in total for key, value in d.items()]
                list(map(lambda intens: dictVar.update(intens), total_dicts))
                self.listOfGetDocumentsDay.append(dictVar)
            except AttributeError:
                continue        
        return self.listOfGetDocumentsDay
    
    def dataGraphAllMonthTotal(self, setor, month):
        self.clearList()
        mes = self.enumsMonthDays.colectMonths(int(month))
        for days in range(mes):
            try:
                document = self.getDocumentFind({"2024": f"{month}", f"{setor}": days})
                agulhas = document.get('AGULHAS', {})
                total = agulhas.get('TOTAL', []) 
                list(map(lambda x: self.listMonthTotalResult.append(x), total))
                #Monthdicts = [{key: value} for d in total for key, value in d.items()]
            except AttributeError:
                continue   
        return self.listMonthTotalResult
    
    #select finura and get total all month
    def dataGraphAllMonth(self, setor, month, finura):
        self.clearList()
        mes = self.enumsMonthDays.colectMonths(int(month))
        for days in range(1 ,mes):
            try:
                document = self.getDocumentFind({"2024": f"{month}", f"{setor}": days})
                agulhas = document.get('AGULHAS', {})
                total = agulhas.get('TOTAL', []) 
                for dictList in total:
                    for key , value in dictList.items():
                        if key == finura:
                            self.listMonthTotalResult.append([{key: value}])
            except AttributeError: 
                self.listMonthTotalResult.append([{"None": 0}])
        return self.listMonthTotalResult
        
    def pizzaDataMonth(self, setor, month):
        data = self.dataGraphMonth(setor, month)
        dataMonthSum = self.monthTotalSum(data)  
        return dataMonthSum
    
    def pizzaDataDay(self, month, setor, day):
        data = self.popDayProducts(month, setor , day)
        return data
    
    def pizzaDataComp(self, month, setor, finura):
        self.clearList()
        mes = self.enumsMonthDays.colectMonths(int(month))
        mesName = self.enumsMonthDays.colectMonthsName(int(month))
        for days in range(1 ,mes):
            try:
                totalSum = collections.defaultdict(int)
                document = self.getDocumentFind({"2024": f"{month}", f"{setor}": days})
                agulhas = document.get('AGULHAS', {})
                total = agulhas.get('TOTAL', []) 
                for dictList in total:
                    for key , value in dictList.items():
                        if key == finura:
                           totalSum[finura]+= value 
                self.listMonthTotalResult.append([totalSum])
                self.listMonthTotalResult.append(mesName)
            except AttributeError: 
                continue
        return self.listMonthTotalResult
    
    #update for xlsx
    def addNewLine(self, month, day, setor, newLineList):
        file_path = self.pathXlxs("2024")
        try:
            # Load the existing file into a DataFrame
            df_existing = pd.read_excel(file_path, engine='openpyxl')
        except FileNotFoundError:
            # If the file does not exist, create a new DataFrame with the appropriate columns
            if setor == "RASCHELL":
                nameTableList =  self.enumsFinuras.finurasXlsx(setor)
                df_existing = pd.DataFrame(columns= nameTableList)
                  
                # Save the DataFrame to an Excel file
                with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                    df_existing.to_excel(writer, sheet_name=f'{month}', index=False)
                    df_updated = pd.concat([df_existing, new_row])

            elif setor == "JACQUARD":
                df_existing = pd.DataFrame(columns= self.enumsFinuras.finurasXlsx(setor))
                
            elif setor == "RASCHELL2":     
                 df_existing = pd.DataFrame(columns= self.enumsFinuras.finurasXlsx(setor))
                
        new_row = pd.DataFrame(newLineList)
        df_updated = pd.concat([df_existing, new_row])

        # Step 3: Save the updated DataFrame to the Excel file (overwrite if it exists)
        df_updated.to_excel(file_path, index=False, engine='openpyxl')
        
        #add turn select
    def addDayDataListXlsx(self, day,  turn, data):
        match turn:
            case "TA":
                if self.conts == 0:
                    self.dictDataXlsx.update({"DIA": day})
                    self.conts += 1
                    self.dictDataXlsx.update(data)
                else:
                    self.dictDataXlsx.update(data)
            case "TB":
                self.dictDataXlsx.update(data)
            case "TC":   
                self.dictDataXlsx.update(data)
            case _:
                return "TURN ERROR "
    
    def keyFinurasAppend(self,turn, finuras):
        if turn == "TA":
            return finuras
        elif turn == "TB":
            return finuras + "TB"
        else :
            return finuras + "TC"
    
    #triger for addDictDAy
    def addDayXlxs(self, month,  day, setor):
        listOfDayData = []
        listOfDayData.append(self.dictDataXlsx)
        newLineList = self.addDictDayXlsx(setor, listOfDayData[0])
        self.addNewLine(month, day, setor, newLineList)
                  
    #add day list for organize in execel turns  
    def addDictDayXlsx(self, setor, data):
        agulhasEnums = self.enumsFinuras.finurasXlsx(setor)
        """
        add finuras total day
        for key, value in data.items():
            print(self.sumList(key, value))
        print(self.sumDay())
        """
        self.funcAddDictTurns(data, agulhasEnums)
              
    #Slice addDictDayXlsx params for simple
    def funcAddDictTurns(self, data, agulhasEnums):
        dayTurn = {}
        daySets = set()
        for agulhas in agulhasEnums:
            for key, value in data.items():
                if key == agulhas:
                    dayTurn.update({agulhas: value})
                    daySets.add(agulhas)
                elif not agulhas in daySets:
                    dayTurn.update({agulhas: None})
        self.clearList()
        self.dayTurnData.append(dayTurn)
        return self.dayTurnData
    
    def pathXlxs(self, year):
        self.path = r"C:\Users\User\Desktop\CURSO PYTON\DiarioPython\new_Teste_pandas.xlsx"
        return self.path
    
    #select day and return list data not empty
    def daySelectDataXlsx(self, month, day):
        dayLine = (day -1)
        path = self.path
        nameSheet = month
        df = pd.read_excel(path, sheet_name=nameSheet)
        # Access the specific row
        rowData = df.iloc[dayLine]
        dataReal = rowData.dropna()
        self.rowDataListDay = list(map(lambda item: {item[0]: item[1]}, dataReal.items()))
        return self.rowDataListDay     
       
        
        
   