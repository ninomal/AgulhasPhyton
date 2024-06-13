from pymongo import MongoClient

class Api():
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
    
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
    