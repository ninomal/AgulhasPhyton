from products.Products import Products
from api.api import Api
from enums.enumsToday import Enumstoday
from IO.io import IO
import pandas as pd



def main():
    #io = IO()
    #io.ioMainLoop()
    
   
    products = Products()
    try:
        products.dayPoPxlsx(9, 12, 'TA')
        products.dayPoPxlsx(9, 12, 'TB')
        products.dayPoPxlsx(9, 12, 'TC')
        products.dayPoPtotalUP(9, 12)
    except TypeError:
        pass
   
   
   
   
    
    
if __name__ == "__main__":
    main()