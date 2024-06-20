from models.conection.conection import DBconection
from models.repository.myConection import MyConection

class Api():
    def __init__(self):
       self.mongoDB = DBconection()                           
       self.mongodbConection = MyConection(self.mongoDB,self.mongoDB.getColection())
        
  
    def addUserMongodb(self, userDataID):
        posts = self.client.posts
        post_id = posts.insert_one(userDataID).inserted_id
        
    def addFinuraMongodbserMongodb(self, finuraData):
        pass
        #add user here
        
    def addAgulhasBrokenMongodbserMongodb(self, agulhasData):
        pass
        #add user here

    def addTotalOfDayMongodb(self, totalOfDay):
        pass
        
    def getFinuras(self):
        pass
    
    def getTotalofDay(self):
        pass
    
    def getMountId(self):
        pass
   
    
    def teste(self):
        teste = {"teste": 14141416789}
        self.mongodbConection.insert_document(teste)
        #dbt_colect = self.mongodbConection.getColection()
        #print(dbt_colect)
    
  