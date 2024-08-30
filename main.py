from products.Products import Products
from api.api import Api
from enums.enumsToday import Enumstoday
from IO.io import IO
import pandas as pd



def main():
    
  
    io = IO()
   
     
    io.ioMainLoop()
    '''
    
    products = Products()
    
    data ={"F12": 5 ,"F14": 5, "F18": 10}
    data1 ={"F12TB": 10 ,"F14TB": 15, "F24PL": 3}
    data2 ={"F12TC": 15 ,"F14TC": 20, "TOTAL3975": 135}
    products.addDayDataListXlsx("TA", data)
    products.addDayDataListXlsx("TB", data1)
    products.addDayDataListXlsx("TC", data2)
   
    products.addDayXlxs(1, "RASCHELL")
    
    teste = products.dayTurnData
    print(teste)
    products.addNewLine(path, teste, "RASCHELL")
    
 
    products.pathXlxs(path)
    products.daySelectDataXlsx("Sheet1", 1)    
 
   
    #This is first version make for test
    
  
    api = Api() 
    #remove
    today = 0
    enumsToday = Enumstoday()
    day = str(input("Digite o Dia: "))
    month = str(input("Digite o Mes: "))
    products = Products(month, day)
    
    def agulhasInput(today):
        setor = "RASCH"
        eraser = "S"
        finurasCheck = False
        inserir = True
        todayEnums = enumsToday.getEnumsToday(today)
        print(todayEnums)
        while inserir:
            try:
                while finurasCheck != True:
                    finuras = str((input("Finura: ")))
                    finurasCheck = products.finuraCheck(finuras)
                    if finurasCheck == False:
                        print("Finura errada")       
            except TypeError:
                print("Type error")
            try :
                while eraser == "S":
                    agulhasBroken = int(input("Agulhas quebradas: "))
                    eraser = str(input(("Agulhas estão erradas? digite s para apagar ")))
                    eraser.upper()
            except ValueError :
                print("Numero invalido")
            finally:
                products.addAgulhasinDictList(todayEnums, finuras, agulhasBroken)
                products.finuraCodeDay(finuras, agulhasBroken)
                products.sumDay()
                answer = input("Vai continuar? digite s: ")
                if answer.upper() != "S":
                    inserir = False  
            
    def addDataMongoDB(setor):
        result = products.addDay(setor)
        products.productService.addDayAgulhaBrokeMongoDB(result)
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
       
  
     
   
    #total day display or not 
    def agulhasBrokenPrint()
        totalDayList = products.getTotalofDay(self):
        for intens in totalDayList:
            print(intens)
    '''
    
    
    
if __name__ == "__main__":
    main()