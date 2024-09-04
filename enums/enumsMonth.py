


class EnumsMonthDays():
    def __init__(self):
        pass
              
    def colectMonths(self, month):
        match month:
            case 1 :
                return 31
            case 2 :
                return 29
            case 3 :
                return 31
            case 4 :
                return 30
            case 5 :
                return 31
            case 6 :
                return 30
            case 7 :
                return 31
            case 8 :
                return 31
            case 9 :
                return 30
            case 10 :
                return 31
            case 11 :
                return 30
            case 12 :
                return 31

    def colectMonthsName(self, month):
        match month:
            case 1:
                return "Janeiro"
            case 2:
                return "Fevereiro"
            case 3:
                return "Março"
            case 4:
                return "Abril"
            case 5:
                return "Maio"
            case 6:
                return "Junho"
            case 7:
                return "Julho"
            case 8:
                return "Agosto"
            case 9:
                return "Setembro"
            case 10:
                return "Outubro"
            case 11:
                return "Novembro"
            case 12:
                return "Dezembro"
            case __:
                return "ERROR"