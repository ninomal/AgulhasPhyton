FINURAS = {"F9","F18" ,"F14" ,"F12" ,"F18PL" ,"F24PL"
        ,"F1869" ,"F1469" ,"F969" ,"F7" ,"F1232","F932","F24KETTEN"}

class EnumsFinuras:
    def __init__(self):
        pass
    
    def finurasEnumsSelect(self, finuras):
        finurasStr = str(finuras)
        finurasUperr = finurasStr.upper()
        match finurasUperr:
            case "F9":
                return 3975
            case "F18":
                return 3975
            case "F14":
                return 3975
            case "F12":
                return 3975
            case "F18PL":
                return 4575
            case "F24PL":
                return 4565
            case "F1869":
                return 4475
            case "F1469":
                return 4496
            case "F969":
                return 4496
            case "F7":
                return 4496
            case "F1232":
                return 2760
            case "F932":
                return 2760
            case "F24KETTEN":
                return 2660
                            
    def checkFinurasEnums(self, check):
        checkStr = str(check)
        checkSet = {checkStr.upper()}
        if FINURAS.intersection(checkSet):
            return ("Finura ok")
        else:
            return ("Finura errada")
                
                            