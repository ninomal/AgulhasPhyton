from api.api import Api


class ProductsService:
    def __init__(self):
        self.api = Api()
     
    def adduserIdMonthId(self, monthIdData):
        self.api.getMountId(monthIdData)      
        
    def addDayAgulhaBrokeMongoDB(self, algulhas):
        self.api.addDayAgulhaMongoDB(algulhas)
        
    def addTotalOfDay(self, totalDay):
        self.api.addTotalOfDayMongodb(totalDay)
    
    def getMountId(self):
        self.api.getMountId()   
        
    def getFinuras(self):
        self.api.getFinuras()
    
    def getTotalofDay(self):
        self.api.getTotalofDay()
    
   
        