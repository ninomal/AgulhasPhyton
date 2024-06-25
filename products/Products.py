from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsMonthNameStr import EnumsMonthNameStr
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
        self.listNeedlesBrokenDay = []  
        
        
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
    
    def addDayMongoDB(self, finuras, agulhas, turno, setor):
        agulhasDict = self.addAgulhasinDictList(finuras, agulhas)
        dayMongo = self.addDay(self.nameColection, setor, turno, agulhasDict)
        return dayMongo
  
    def addDay(self, day , setor, turno,  agulhasDictList ):
        dayStr = str(day)
        dictDay = {dayStr : {setor :{turno: agulhasDictList}}}
        return dictDay
             
    def convertFinurasInCodeBar(self, finuras, agulhas):
        finurasDict = {finuras: agulhas}
        return finurasDict
        
    def addAgulhasinDictList(self, finuras, agulhasData ):
        self.listNeedlesBrokenDay.append({finuras : agulhasData})
        return self.listNeedlesBrokenDay
    
    def clearList(self):
        self.listNeedlesBrokenDay = []
        
    def sumOfDay(self, data : Dict) -> Dict:
        result = dict(functools.reduce(operator.add,
                        map(collections.Counter, data)))
        return result
    