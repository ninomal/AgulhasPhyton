from products.Products import Products
from api.api import Api
from enums.enumsToday import Enumstoday
from IO.io import IO
import pandas as pd



def main():
    io = IO()
    io.ioMainLoop()
    
    '''
    products = Products()
    try:
        print(products.popDayProducts(9, "RASCHELL", 12, "XLSX"))
    except TypeError:
        print("ERRORR")
        pass'''
   
   
   
   
    
    
if __name__ == "__main__":
    main()