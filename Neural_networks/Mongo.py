import pymongo, datetime,bson,time
from numpy import array, dot, random

from pymongo import MongoClient

class Mongo:
    __client	= None
    __db 		= None
    __colletion	= None

    def __init__(self,db='dynamic',address='localhost',port=27017):
        self.__client		= MongoClient('localhost', 27017)
        self.__db			= self.__client['dynamic']
        self.__colletion 	= self.__db['results']

    def insertResults(self,results):
        for result in results:
            self.__colletion.insert_one({'weights':result['weights'].tolist(),'result':result['result'],'false_negative':result['false_negative'],'number':result['number'],'time':result['time'],'false_positive':result['false_positive'],'negative':result['negative'],'positive':result['positive']})

    def getResults(self):
        self.__colletion = self.__db['results']
        return self.__colletion.find().sort("_id")
