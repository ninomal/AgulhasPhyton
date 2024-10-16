from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsFinuras import EnumsFinuras
from enums.enumsToday import Enumstoday
from typing import Dict
import collections, functools, operator, random
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
from pathlib import Path
import os
import numpy

RASCHELLIST = [3975, 4575, 4475, 4565]
JAQUARDLIST = [4496, 2760]
KETEN = [2660]

class Products():
    def __init__(self) :
        self.monthTotalDict = {}
        self.productService = ProductsService()
        self.enumsMonthDays = EnumsMonthDays()
        self.enumsFinuras = EnumsFinuras()
        self.enumsToday = Enumstoday()
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
        self.path = self.pathXlxs()
        
       
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
    def sumList(self, finura, agulha, dataMode):
        if dataMode == "MongoDB":
            finuraCode = self.enumsFinuras.finurasCodeReturn(finura)
        else:
            finuraCode = self.enumsFinuras.finurasCodeReturnXlsx(finura)
        result_dict = {finuraCode: agulha}
        self.listSumNedlleDict.append(result_dict)
        return self.listSumNedlleDict
   
    def randImage(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = Path(fr'AgulhasPhyton\IO\image\ess{randInt}.png')
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
      
    def popDayProducts(self, month, setor, day, dataMode):
        self.clearList()
        dictVar = {}
        if dataMode == "MongoDB":
            try:
                #TA
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
        else:
            try:
                self.dayPoPxlsx(month, day, setor)
                self.dayPoPtotalUP(month, day, setor)
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
    
    def pizzaDataDay(self, month, setor, day, dataMode):
        data = self.popDayProducts(month, setor , day, dataMode)
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
    
    def getEnumsFinuras(self, setor):
        return self.enumsFinuras.finurasXlsx(setor)
    
    def getEnumsTotal(self):
        return self.enumsFinuras.finurasCodeTotal()
    
    def getEnumsSetorNames(self, setorRange):
        return self.enumsToday.getEnumsSetorNames(setorRange)
    
    #update for xlsx
    def addNewLine(self,setorGet, month, newLineList):
        month_name = self.enumsMonthDays.colectMonthsName(int(month))
        setor = setorGet + month_name
        file_path = self.pathXlxs()
        #month = self.enumsMonthDays.colectMonthsName(int(month))
        # Load the existing file into a DataFrame
        try:
            df_existing = pd.read_excel(file_path, engine='openpyxl')
        except FileNotFoundError:
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            
        # Get the column names
        nameTableList = self.enumsFinuras.getAllFinurasXlsx()
        df_existing = pd.DataFrame(columns=nameTableList)   

        # Create a new DataFrame from the new row data
        new_row = pd.DataFrame(newLineList)

        # Save the DataFrame to an Excel file for the first time
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df_existing.to_excel(writer, sheet_name=month, index=False)
            df_existing = pd.concat([df_existing, new_row], ignore_index=True)
            df_existing.to_excel(writer, sheet_name=month, index=False)

        # Update the existing DataFrame
        try:
            new_row = pd.DataFrame(newLineList)
            df_existing = pd.concat([df_existing, new_row], ignore_index=True)

            # Save the updated DataFrame back to the same sheet
            with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
                df_existing.to_excel(writer, sheet_name=month, index=False)

            return ("\nUpdated DataFrame:", df_existing)
        except Exception as e:
            return (f"Error saving the file: {e}")
            
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
            
    def totalAddXlsx(self):
        return self.dictDataXlsx.update(self.listSumDayResult[0])
    
    def keyFinurasAppend(self,turn, finuras):
        if turn == "TA":
            return finuras
        elif turn == "TB":
            return finuras + "TB"
        else :
            return finuras + "TC"
    
    #triger for addDictDAy
    def addDayXlxs(self, month, day, setor):
        listOfDayData = []
        self.totalAddXlsx()
        listOfDayData.append(self.dictDataXlsx)
        newLineList = self.addDictDayXlsx(setor,day, listOfDayData[0])
        self.addNewLine(setor, month, newLineList)
                  
    #add day list for organize in execel turns  
    def addDictDayXlsx(self, setor, day, data):
        agulhasEnums = self.enumsFinuras.finurasXlsxAddDAY(setor)
        dataSelect = self.funcAddDictTurns(data, agulhasEnums)
        return dataSelect
              
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
                    dayTurn.update({agulhas: numpy.nan})
        self.dayTurnData.append(dayTurn)
        self.clearList()
        return self.dayTurnData
    
    def pathXlxs(self):
        self.path = f"C:/Users/ninomal/Documents/phyton projetos/diariohPhyton/AgulhasPhyton/{self.year}.xlsx"
        return self.path
    
    #select day and return list data not empty
    def daySelectDataXlsx(self, month, day):
        try:
            enumsMonth = self.enumsMonthDays.colectMonthsName(int(month))
            df = pd.read_excel(self.path, sheet_name=enumsMonth)
            rowData = df[df['DIA']== day]
            self.rowDataListDay.append(rowData.to_dict(orient='records'))
            return self.rowDataListDay[0]     
        except ValueError:
            return "Valuer ERROR"
        except IndexError:
            return "INDEX ERROR"
      
    #select month and return list data not empty
    def monthSelectDataXlsx(self, month):
        try:
            enumsMonth = self.enumsMonthDays.colectMonthsName(month)
            df = pd.read_excel(self.path, sheet_name=enumsMonth)
            dfRowsLen = len(df)
            for days in range(dfRowsLen):
                rowData = df.iloc[days -1]
                dataReal = rowData.dropna()
                self.rowDataListDay = list(map(lambda item: {item[0]: item[1]}, dataReal.items()))
            return self.rowDataListDay 
        except ValueError:
            return "Valuer ERROR"
        except IndexError:
            return "INDEX ERROR"     
    
    #Output data for pop day display          
    def dayPoPxlsx(self, month, day, setor):  
        dictDay = {}
        data = self.daySelectDataXlsx(month, day)[0]
        finurasSetor = self.enumsFinuras.finurasXlsx(setor)
        for turn in self.enumsToday.getEnumsTurns():
            finurasTurn = self.enumsFinuras.finurasTurnXlsx(turn)
            for keys , value in data.items():
                if ((keys in finurasTurn) and value > 0) and keys in finurasSetor:
                    key = self.eraseTurnName(turn, keys)
                    dictDay.update({key: value}) 
            self.listOfGetDocumentsDay.append(dictDay)
            dictDay = {}        
        return self.listOfGetDocumentsDay
     
    #Add day total 
    def dayPoPtotalUP(self, month , day, setor):
        dictDay = {}
        data = self.daySelectDataXlsx(month, day)[0]
        finurasCode = self.enumsFinuras.finurasCodeTotal()
        finurasSetor = self.enumsFinuras.finurasXlsx(setor)
        for keys , value in data.items():
           if ((keys in finurasCode) and value > 0) and keys in finurasSetor:
               key = keys.split("T")[1]
               dictDay.update({key: value})
        self.listOfGetDocumentsDay.append(dictDay)
        dictDay = {}
        return self.listOfGetDocumentsDay
    
    #pop Diagrafico
    def popDiagraficoXlsx(self, month, day):
        for setor in self.enumsToday.getSetorNames():
            self.dayPoPxlsx(month, day, setor)
            self.dayPoPtotalUP(month , day, setor)
            return  self.listOfGetDocumentsDay
        
    
    def eraseTurnName(self,turn, key):    
        match turn:
            case "TA":
                return key
            case "TB":
                keySplit = key.split("TB") 
                return keySplit[0]
            case "TC":
                keySplit = key.split("TC") 
                return keySplit[0]
    