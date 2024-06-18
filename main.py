from products.Products import Products
from api.api import Api
from enums.enumsFinuras import EnumsFinuras


def main():
    teste = "f18"
    teste2 = "f32"
    api = Api()
    api.teste()
    enumsFinuras = EnumsFinuras()
    print(enumsFinuras.checkFinurasEnums(teste))
    print(enumsFinuras.checkFinurasEnums(teste2))
    print(enumsFinuras.finurasEnumsSelect(teste))
    
    """
    today = 0
    enumsToday = Enumstoday()
    day = int(input("Digite o Dia: "))
    month = int(input("Digite o Mes: "))
    products = Products(month, DAY)
    
    def agulhasInput(today):
        inserir = True
        todayEnums = enumsToday.getEnumsToday(today)
        print(todayEnums)
        while inserir:  
            finura = str((input("Finura: ")))
            agulhasBroken = int(input("Agulhas quebradas: "))
            asw = input("Vai continuar? digite s: ")
            if asw.upper() != "S":
                inserir = False
                            
    print("Raschell")
    for today in range(3):
        agulhasInput(today)
    
    print("Jacquard")
    for today in range(3):
        agulhasInput(today)
        
    #total day display or not 
        """
        
    
    
if __name__ == "__main__":
    main()