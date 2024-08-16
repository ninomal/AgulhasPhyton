from products.Products import Products
from api.api import Api
from enums.enumsToday import Enumstoday
from IO.io import IO



def main():

   
    file_path = r"C:\Users\User\Desktop\CURSO PYTON\DiarioPython\new_Teste_pandas.xlsx"
    products = Products()
    
    newLine = [{'Dia':5,'F9': 15, "F12": 1, "F14":None, "F24": 2 }]
    products.addNewLine(file_path, newLine)
  
    
       
    #io = IO()
   
     
    #io.ioMainLoop()
    
    #products = Products()
    #products.popDayProducts()
        

    
    """
    """
    """
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
    """
        
    
    
    
if __name__ == "__main__":
    main()