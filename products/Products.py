from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsMonthNameStr import EnumsMonthNameStr
from enums.enumsFinuras import EnumsFinuras
from enums.enumsFinuras import EnumsFinuras
from typing import Dict
import collections, functools, operator

RASCHELLIST = [3975, 4575, 4475, 4565]
JAQUARDLIST = [4496, 2760]
KETEN = [2660]

class Products():
    def __init__(self, month, day) :
        self.day = str(day)
        self.month = str(month)
        self.nameColection = self.day + self.month
        self.monthTotalDict = {}
        self.productService = ProductsService()
        self.enumsMonthDays = EnumsMonthDays()
        self.enumsMonthNameStr = EnumsMonthNameStr()
        self.monthStr = self.enumsMonthNameStr.colectMonthsName(month)
        self.monthDays = self.enumsMonthDays.colectMonths(month)
        self.enumsFinuras = EnumsFinuras()
        self.enumsFinuras = EnumsFinuras()
        self.listNeedlesBrokenDayTA = [] 
        self.listNeedlesBrokenDayTB = []  
        self.listNeedlesBrokenDayTC = [] 
        self.listSumNedlleDict = []
        
        
    def monthTotal(self, month):   
        #finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()
        monthName = self.enumsMonthNameStr.colectMonthsName(month)
        monthDays = self.enumsMonthDays.colectMonths(month)
        self.monthTotalDict["Month"] = monthName
        for finuras in RASCHELLIST:
            #take total in mongodb
            self.monthTotalDict["Raschell"] = {finuras : total} 
        for finuras in JAQUARDLIST:
            #take total in mongodb
            self.monthTotalDict["Jacquard"] = {finuras : total} 
        for finuras in KETEN:
            #take total in mongodb
            self.monthTotalDict["Keten"] = {finuras : total}       
        return  self.monthTotalDict
        #cross the id and colect finuras in month
    
    def totalDay(self, finuraInput, day):
        finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()   
        return (f"O dia ",day,"\n A finura ", finuraGet," quebrou o total de: ", total)
      
    def monthSlectID(self):
        return (self.day + self.enumsMonthNameStr)
    
    def eraseTurn(self, day, month, turn):
        #select turn and re write
        pass
    
    def deletDaySelect(self):
        #delete day here
        pass
    
    def selectMonthgrafics(self, month):
        #select month to se grafics
        pass
    
    def monthComparation(self, month1, month2):
        #select the month for comparation
        pass
    
    def addDayMongoDB(self, setor):
        dayMongo = self.addDay( setor)
        return dayMongo
  
    def addDay(self,  setor)->Dict:
        dictDay = {self.nameColection : {setor :{"TA": self.listNeedlesBrokenDayTA,
                                     "TB": self.listNeedlesBrokenDayTB, 
                                     "TC": self.listNeedlesBrokenDayTC,
                                     "total": self.listSumNedlleDict}}}
        return dictDay
             
    def convertFinurasInCodeBar(self, finuras, agulhas):
        finurasDict = {finuras: agulhas}
        return finurasDict
        
    def addAgulhasinDictList(self, turno, finuras, agulhasData ):
        match(turno):
            case "TA":
                self.listNeedlesBrokenDayTA.append({finuras : agulhasData})
                return self.listNeedlesBrokenDayTA
            case "TB":
                self.listNeedlesBrokenDayTB.append({finuras : agulhasData})
                return self.listNeedlesBrokenDayTB
            case "TC":
                self.listNeedlesBrokenDayTC.append({finuras : agulhasData})
                return self.listNeedlesBrokenDayTC
            
    def clearList(self):
        self.listNeedlesBrokenDayTA = []
        self.listNeedlesBrokenDayTB = []
        self.listNeedlesBrokenDayTC = []
        self.listSumNedlleDict = []
        
    def sumDay(self, finura, agulha):  
        finurasCode = self.enumsFinuras.finurasCodeReturn(finura)
        match finurasCode:
            case "3975":
                self.listSumNedlleDict.append({"3975": agulha })
            case"4575":
                self.listSumNedlleDict.append({"4575": agulha })
            case "4496":
                self.listSumNedlleDict.append({"4496" : agulha})
            case "2660":
                self.listSumNedlleDict.append({"2660" : agulha})
            case "2670":
                self.listSumNedlleDict.append({"2670" : agulha})
            case "4565":
                self.listSumNedlleDict.append({"4565" : agulha})
            case _:
                return "ERROR"
            
    