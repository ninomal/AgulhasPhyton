FINURAS = {"F9","F18" ,"F14" ,"F12" ,"F18PL" ,"F24PL"
        ,"F1869" ,"F1469" ,"F969" ,"F7" ,"F1232","F932","F24KET"}
FINURASCODE = {"3975", "4565", "4575", "4475", "4496", "2760", "2660"}
FINURAS3975 = {"F9","F18" ,"F14" ,"F12"} 
FINURAS4496 = {"F1469" ,"F969" ,"F7" }
FINURAS2660 = {"F1232","F932"}
FINURAF18PL = "F18PL"
FINURA24KET = "F24KET"
FINURA24RAS = "F24PL"
FINURASXLSXRASCHELL =  ["DIA", "F9", "F9PL","F12", "F1269",
                                "F14","F18", "F18PL", "F24PL", "F1869",
                        "F9TB", "F9PLTB","F12TB", "F1269TB",
                            "F14TB","F18TB", "F18PLTB", "F24PLTB", "F1869TB",
                        "F9TC", "F9PLTC","F12TC", "F1269TC",
                            "F14TC","F18TC", "F18PLTC", "F24PLTC", "F1869TC","TOTAL",
                            "T3975", "T4575", "T4565", "T4475"]

FINURASXLSRASCHELL2 = ["DIA","F9", "F12", "F14", "F18",
                       "F9TB", "F12TB", "F14TB", "F18TB",
                       "F9TC", "F12TC", "F14TC", "F18TC",
                       "TOTAL","T3975"]

FINURASXLSJACQUARD = ["DIA",'F7','F969','F1232','F1432',
                    'F7TB','F969TB','F1232TB', 'F1432TB',
                    'F7TC','F969TC','F1232TC', 'F1432TC',
                    'TOTAL','T4496','T2760']

FINURASXLSKET = ["DIA","F24KET", "F24KETTB","F24KETTC",
                 "TOTAL", "T2660"]


class EnumsFinuras:
    def __init__(self):
        self.FINURASCODE = FINURASCODE
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
        finurasUpper = finurasStr.upper()
        if finurasUpper in FINURAS3975:
            return "3975"
        elif finurasUpper == "F1869":
            return "4475"
        elif finurasUpper == "F18PL":
            return "4575"
        elif finurasUpper == "F24PL":
            return "4565"
        elif finurasUpper in FINURAS4496:
            return "4496"
        elif finurasUpper in FINURAS2660:
                return "2660"
        elif finurasUpper == "F24KET":
            return "2660"
        else :
            return "ERROR"

    def finurasCodeReturnXlsx(self, finuras):
            finurasStr = str(finuras)
            finurasUpper = finurasStr.upper()
            if finurasUpper in FINURAS3975:
                return "T3975"
            elif finurasUpper == "F1869":
                return "T4475"
            elif finurasUpper == "F18PL":
                return "T4575"
            elif finurasUpper == "F24PL":
                return "T4565"
            elif finurasUpper in FINURAS4496:
                return "T4496"
            elif finurasUpper in FINURAS2660:
                    return "T2660"
            elif finurasUpper == "F24KET":
                return "T2660"
            else :
                return "ERROR"
        
    def finurasXlsx(self, setor):
        match setor:
            case  "RASCHELL":
                return FINURASXLSXRASCHELL
            case "JACQUARD":
                return FINURASXLSJACQUARD
            case "KETTEN":
                return FINURASXLSKET
            case "RASCHELL2":
                return FINURASXLSRASCHELL2
        
    