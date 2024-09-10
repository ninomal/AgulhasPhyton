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
        print(products.monthSelectDataXlsx(9))
    except TypeError:
        pass
   
   
   
   
    
    
if __name__ == "__main__":
    main()