import pymongo
from pymongo.errors import ConnectionFailure
from bson import ObjectId
from django.conf import settings
from .exceptions import WeatherException

class WeatherRepository:

    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def getConnection(self):
        try:
            client = pymongo.MongoClient(
                getattr(settings, "MONGO_CONNECTION_STRING")
            )
        except ConnectionFailure as e :
            raise WeatherException(f"Error connecting to database: {e}")
        
        connection = client[
            getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self):
        documents = []
        for document in self.getCollection().find({}):
            id = document.pop('_id')
            document['id'] = str(id)
            documents.append(document)
        return documents
    
    def get(self, filter):
        documents = []
        for document in self.getCollection().find(filter):
            id = document.pop('_id')
            document['id'] = str(id)
            documents.append(document)
        return documents
    
    def getByID(self, id):
        document = self.getCollection().find_one({"_id": ObjectId(id)})
        id = document.pop('_id')
        document['id'] = str(id)
        return document
    
    def insert(self, document):
        self.getCollection().insert_one(document)

    def update(self, document, id):
        self.getCollection().update_one({"_id": ObjectId(id)}, 
                                       {"$set": document})

    def deleteAll(self):
        self.getCollection().delete_many({})

    def deleteByID(self, id):
        ret = self.getCollection().delete_one({"_id": ObjectId(id)})
        return ret.deleted_count