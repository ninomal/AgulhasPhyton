from products.Products import Products
from api.api import Api
from enums.enumsFinuras import EnumsFinuras
from enums.enumsToday import Enumstoday


def main():
    api = Api()
    enumsFinuras = EnumsFinuras()
    
    products = Products("01", "07")
    name = {"teste": 12345}
    iten = products.productService.getTotalofDay(name)
    for items in iten:
        print(items)
    
    """  
    today = 0
    enumsToday = Enumstoday()
    day = str(input("Digite o Dia: "))
    month = str(input("Digite o Mes: "))
    products = Products(month, day)
    
    def agulhasInput(today):
        inserir = True
        todayEnums = enumsToday.getEnumsToday(today)
        print(todayEnums)
        while inserir:  
            finuras = str((input("Finura: ")))
            finuras = finuras.upper()
            agulhasBroken = int(input("Agulhas quebradas: "))
            products.addAgulhasinDictList(todayEnums, finuras, agulhasBroken)
            products.sumDay(finuras, agulhasBroken)
            answer = input("Vai continuar? digite s: ")
            if answer.upper() != "S":
                inserir = False  
     
    def addDataMongoDB(setor):
        result = products.addDay(setor)
        products.productService.addDayAgulhaBrokeMongoDB(result)
        print(products.listSumNedlleDict)
        products.clearList()
                           
    print("Raschell")
    setor = "RASCH"
    for today in range(3):
        agulhasInput(today)
    addDataMongoDB(setor)
   
      
    print("Jacquard")
    setor = "JACQ"
    for today in range(3):
        setor 
        agulhasInput(today)
    addDataMongoDB(setor)
       
    """
     
    """
    #total day display or not 
    def agulhasBrokenPrint()
        totalDayList = products.getTotalofDay(self):
        for intens in totalDayList:
            print(intens)
    """
        
    
    
    
if __name__ == "__main__":
    main()