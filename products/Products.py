from productsService.productsService import ProductsService
from enums.enumsMonth import EnumsMonthDays
from enums.enumsMonthNameStr import EnumsMonthNameStr

class Products():
    def __init__(self) :
        self.productService = ProductsService()
        self.enumsMonth = EnumsMonthDays()
        self.enumsMonthNameStr = EnumsMonthNameStr()
        
    def monthTotal(self):
        finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()
        day = self.productService.getMountId() 
        #cross the id and colect finuras in month
    
    def totalDay(self, finuraInput):
        finuraGet = self.productService.getFinuras()
        total = self.productService.getTotalofDay()
        day = self.productService.getMountId()   
        return (f"O dia ",day,"\n A finura ", finuraGet," quebrou o total de: ", total)
      
    def monthSlectID(self, month):
        pass
        
    def teste(self):
        self.enumsMonth.colectMonths()
    
    