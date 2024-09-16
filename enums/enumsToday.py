TURNS = ["TA", "TB", "TC"]

class Enumstoday:
    def __init__(self):
        pass    
        
    def getEnumsToday(self, turn):
        match turn:
            case 0:
                return "TA"
            case 1:
                return "TB"
            case 2:
                return "TC"
            case _:
                return "turn ERROR"
            
    def getEnumsSetorNames(self, turn):
        match turn:
            case 0:
                return "RASCHELL"
            case 1:
                return "JACQUARD"
            case 2:
                return "KETTEN"
            case _:
                return "turn ERROR"
            
    def getEnumsTurns(self):
        return TURNS