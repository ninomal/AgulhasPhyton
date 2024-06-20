from models.conection import DBconection


class Api():
    def __init__(self):
       self.mongoDBConect = DBconection()                           
       self.colection = self.mongoDBConect.getColection()
        
  
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
    
    def insert(self, name, data):
        self.colection.insert_one({name :data})
    
    def teste(self):
        self.insert("teste", 14141416)
        dbt_colect = self.colection     
        print(dbt_colect)
    
  