from pymongo import MongoClient

class Api():
    def __init__(self):
        self.conectionString = "mongodb://localhost:27017/?directConnection=true"
        self.conectOn = MongoClient(self.conectionString)
        self.conected = self.conectOn['agulhasData']
        self.colection = self.conected.get_collection("AgulhasCollection")
        #self.client = MongoClient("localhost", 27017)
        
    
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
        self.insert("teste", 123456)
        dbt_colect = self.colection     
        print(dbt_colect)
    
  