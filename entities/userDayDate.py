class UserDayData():
    def __init__(self, dayMonth, finura, agulhasBroke):
        self.IDdayMonth = dayMonth
        self.finuraStr = finura
        self.agulhasBroke = agulhasBroke
        
    def getDayMonth(self):
      return self.IDdayMonth
  
    def getFinuraStr(self):
        return self.finuraStr
    
    def getAgulhasBroke(self):
        return self.finuraStr