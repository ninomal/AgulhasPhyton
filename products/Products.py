from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsMonthNameStr import EnumsMonthNameStr
from enums.enumsFinuras import EnumsFinuras
from typing import Dict
import collections, functools, operator, random



RASCHELLIST = [3975, 4575, 4475, 4565]
JAQUARDLIST = [4496, 2760]
KETEN = [2660]

class Products():
    def __init__(self) :
        self.monthTotalDict = {}
        self.productService = ProductsService()
        self.enumsMonthDays = EnumsMonthDays()
        self.enumsMonthNameStr = EnumsMonthNameStr()
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
    
    def monthTotalSum(self, data): 
        totalSum = collections.defaultdict(int)
        for nedlleList in data:
            for key, value in nedlleList.items():
                totalSum[key] += value
        [{'{}'.format(key): value}for key, value in totalSum.items()]
        self.listSumMonthResult.append(dict(totalSum))
        return self.listSumMonthResult
            
    #Check
    def totalDay(self, finuraInput, day):
        finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()   
        return (f"O dia ",day,"\n A finura ", finuraGet," quebrou o total de: ", total)
 
    def addDayMongoDB(self, setor):
        dayMongo = self.addDay( setor)
        return dayMongo
  
    def addDay(self, month, day, setor)->Dict:
        dictDay= {self.year:month, setor : day, "AGULHAS":
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
        monthDays = self.enumsMonthDays(month)
        return monthDays
    
    def monthComparation(self, month1, month2):
        month1Days = self.enumsMonthDays(month1)  
        month2Days = self.enumsMonthDays(month2)
        monthListComp = [month1Days, month2Days]
        return monthListComp
    
    def monthGraphics(self, month):
        monthResult = self.enumsMonthDays.colectMonths(month)
        return monthResult
    
    def getDocumentFind(self, name):
        document = self.productService.getDocumentFind(name)
        return document
    
   
    def popDayProducts(self,day, setor):
        self.clearList()
        #TA
        dictVar = {}
        document = self.getDocumentFind({"2024": day, f"{setor}": 30})
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
    
    #need add days clear add adiocinar pop
    def dataGraphAllMonth(self, setor, month):
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
     
        
    