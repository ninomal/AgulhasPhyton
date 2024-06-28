from products.Products import Products
from api.api import Api
from enums.enumsFinuras import EnumsFinuras
from enums.enumsToday import Enumstoday
from enums.enumsInserir import EnumsInserir


def main():
    api = Api()
    enumsFinuras = EnumsFinuras()
    products = Products("01", "06")
    agulha = 12
    for x in range(10):
        finura = "F14"   
        products.sumDay(finura, agulha)
        agulha +=14
        print(products.listSumNedlleDict)
    
    
    """
    
    today = 0
    enumsToday = Enumstoday()
    day = str(input("Digite o Dia: "))
    month = str(input("Digite o Mes: "))
    products = Products(month, day)
    
    def agulhasInput(today):
        inserirEnums = EnumsInserir().INSERIR
        todayEnums = enumsToday.getEnumsToday(today)
        print(todayEnums)
        while inserir:  
            finuras = str((input("Finura: ")))
            finuras = finuras.upper()
            agulhasBroken = int(input("Agulhas quebradas: "))
            products.addAgulhasinDictList(todayEnums, finuras, agulhasBroken)
            answer = input("Vai continuar? digite s: ")
            if answer.upper() != "S":
                inserirEnums.NAOINSERIR        
        result = products.addDay(setor)
        products.productService.addDayAgulhaBrokeMongoDB(result)
        products.clearList()
     
                           
    print("Raschell")
    for today in range(3):
        setor = "RASCH"
        agulhasInput(today)
    
    
    print("Jacquard")
    for today in range(3):
        setor = "Jac"
        agulhasInput(today)"""
     
    """
    #total day display or not 
    def agulhasBrokenPrint()
        totalDayList = products.getTotalofDay(self):
        for intens in totalDayList:
            print(intens)
    """
        
    
    
    
if __name__ == "__main__":
    main()