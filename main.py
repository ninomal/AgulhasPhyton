from products.Products import Products
from api.api import Api
from enums.enumsToday import Enumstoday
from IO.io import IO
import pandas as pd



def main():

   
    file_path = r"C:\Users\User\Desktop\CURSO PYTON\DiarioPython\new_Teste_pandas.xlsx"
    products = Products()
    
    newLine = {'Dia':5,'F9': 15, "F12": 1, "F24PL": 2 }
    #products.addNewLine(file_path, newLine)
    
    products.addDictDayXlsx(newLine, "RASCHELL")
    """
    # Step 1: Read the existing Excel file into a DataFrame
    
    
    try:
        # Load the file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
        
        # Step 2: Print the specific row (line 4)
        # Note: DataFrame indexing is 0-based, so line 4 is index 3
        if len(df) >= 4:
            print("Line 4 data:")
            print(df.iloc[3])  # Index 3 for line 4
            teste = df.iloc[3]
            print("teste")
            print(type(teste))
            print(teste["F9"])
            print("foi")
            aa = "F12"
            print(type(teste["F12"]))
            print(teste["F12"])
        else:
            print("The DataFrame does not have a fourth row.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    """   
       
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