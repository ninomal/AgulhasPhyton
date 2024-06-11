from enums.enumsToday import Enumstoday

def main():
    today = 0
    enumsToday = Enumstoday()
    
    dayMonth = int(input("Digite o dia e o mes: "))
    
    def agulhasInput(today):
        inserir = True
        todayEnums = enumsToday.getEnumsToday(today)
        print(todayEnums)
        while inserir:  
            finura = int((input("Finura: ")))
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
        
    #total day
        
        
    
    
if __name__ == "__main__":
    main()