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
        
    #need remake
    def monthTotal(self, month):   
        #finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()
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
 
    def addDayMongoDB(self, setor):
        dayMongo = self.addDay( setor)
        return dayMongo
  
    def addDay(self, month, day, setor)->Dict:
        dictDay= {self.year:month, setor : day, "Agulhas":
                                    {"TA": self.listNeedlesBrokenDayTA,
                                     "TB": self.listNeedlesBrokenDayTB, 
                                     "TC": self.listNeedlesBrokenDayTC,
                                     "total": self.listSumNedlleDict}}
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
        
    def finuraCodeDay(self, finura, agulha):  
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
            
    def finuraCheck(self, finuras):
        return self.enumsFinuras.checkFinurasEnums(finuras)
            
    def sumDay(self):
        aggregated = collections.defaultdict(int)
        # Aggregate the values for each key using reduce and lambda function
        for nedlleList in self.listSumNedlleDict:
            for key, value in nedlleList.items():
                aggregated[key] += value
        self.listSumNedlleDict = [{'{}'.format(key): value} for key, value in aggregated.items()]
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
        return month
    
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
    
    def getDaySetor(self, month , setor, day):
        self.productService.getDay(month , setor, day)