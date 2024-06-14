from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsMonthNameStr import EnumsMonthNameStr

RASCHELLIST = [3975, 4575, 4475, 4565]
JAQUARDLIST = [4496, 2760]
KETEN = [2670]

class Products():
    def __init__(self, month, day) :
        self.day = day
        self.monthTotalDict = {}
        self.productService = ProductsService()
        self.enumsMonthDays = EnumsMonthDays()
        self.enumsMonthNameStr = EnumsMonthNameStr()
        self.monthStr = self.enumsMonthNameStr(month)
        self.monthDays = self.enumsMonthDays(month)
        
        
    def monthTotal(self, month):   
        #finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()
        monthName = self.enumsMonthNameStr(month)
        monthDays = self.enumsMonthDays(month)
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
        
   
    
    