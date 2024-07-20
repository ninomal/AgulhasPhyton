FINURAS = {"F9","F18" ,"F14" ,"F12" ,"F18PL" ,"F24PL"
        ,"F1869" ,"F1469" ,"F969" ,"F7" ,"F1232","F932","F24KETTEN"}

FINURAS3975 = {"F9","F18" ,"F14" ,"F12"} 
FINURAS4496 = {"F1469" ,"F969" ,"F7" }
FINURAS2660 = {"F1232","F932"}
FINURAF18PL = "F18PL"
FINURA24KET = "F24KET"
FINURA24RAS = "F24PL"

class EnumsFinuras:
    def __init__(self):
        self.FINURAS = FINURAS
        self.FINURAS3975 = FINURAS3975
        self.FINURAS4496 = FINURAS4496
        self.FINURAS2660 = FINURAS2660
        self.FINURAF18PL = "F18PL"
        self.FINURA24KET = "F24KET"
        self.FINURA24RAS = "F24PL"
        
    
    def finurasEnumsSelect(self, finuras):
        finurasStr = str(finuras)
        finurasUperr = finurasStr.upper()
        match finurasUperr:
            case "F9":
                return "3975"
            case "F18":
                return "3975"
            case "F14":
                return "3975"
            case "F12":
                return "3975"
            case "F18PL":
                return "4575"
            case "F24PL":
                return "4565"
            case "F1869":
                return "4475"
            case "F1469":
                return "4496"
            case "F969":
                return "4496"
            case "F7":
                return "4496"
            case "F1232":
                return "2760"
            case "F932":
                return "2760"
            case "F24KETTEN":
                return "2660"
                            
    def checkFinurasEnums(self, check):
        checkStr = str(check)
        checkSet = {checkStr.upper()}
        if FINURAS.intersection(checkSet):
            return True
        else:
            return False
                
    def finurasCodeReturn(self, finuras):
        finurasStr = str(finuras)
        if (finurasStr.upper()) in FINURAS3975:
            return "3975"
        elif finuras == "F18PL":
            return "4575"
        elif finuras == "F24PL":
            return "4565"
        elif finuras in FINURAS4496:
            return "4496"
        elif finuras in FINURAS2660:
                return "2660"
        elif finuras == "F24KET":
            return "2670"
        else :
            return "ERROR"