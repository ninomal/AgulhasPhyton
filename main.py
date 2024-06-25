from products.Products import Products
from api.api import Api
from enums.enumsFinuras import EnumsFinuras


def main():
    api = Api()
    enumsFinuras = EnumsFinuras()
    
  
    """
    today = 0
    enumsToday = Enumstoday()
    day = int(input("Digite o Dia: "))
    month = int(input("Digite o Mes: "))
    products = Products(month, day)
    
    def agulhasInput(today):
        inserir = True
        todayEnums = enumsToday.getEnumsToday(today)
        print(todayEnums)
        while inserir:  
            finuras = str((input("Finura: ")))
            agulhasBroken = int(input("Agulhas quebradas: "))
            products.addAgulhasinDictList(finuras, agulhasBroken)
            asw = input("Vai continuar? digite s: ")
            if asw.upper() != "S":
                inserir = False           
        exemple  add object here
        result = products.addDayMongoDB()
        products.productService.addDayAgulhaBrokeMongoDB(result)
        products.clearList()
                            
    print("Raschell")
    for today in range(3):
        agulhasInput(today)
    
    print("Jacquard")
    for today in range(3):
        agulhasInput(today)
        
    #total day display or not 
    def agulhasBrokenPrint()
        totalDayList = products.getTotalofDay(self):
        for intens in totalDayList:
            print(intens)
    
        """
        
    
    
if __name__ == "__main__":
    main()