# -*- coding: utf-8 -*-
import csv
import pymongo, datetime,bson,time
from numpy import array, dot, random
from Perceptron import Perceptron
from Mongo import Mongo


if __name__ == "__main__":
    mongo = Mongo()
    myfile = open('result.csv', 'wb')
    wr = csv.writer(myfile,delimiter=',', quoting=csv.QUOTE_ALL)

    data = mongo.getResults()
    i = 0
    for row in data:
        if i == 0:
            wr.writerow(['eta 0.15','','','','','','','',''])
            wr.writerow(['Número','positive','negative','false positive','false negative','accuracy','precision','recall','true_negative'])
        elif i == 10:
            wr.writerow(['eta 0.2','','','','','','','',''])
            wr.writerow(['Número','positive','negative','false positive','false negative','accuracy','precision','recall','true_negative'])
        elif i == 20:
            wr.writerow(['eta 0.3','','','','','','','',''])
            wr.writerow(['Número','positive','negative','false positive','false negative','accuracy','precision','recall','true_negative'])
        elif i == 30:
            wr.writerow(['eta 0.4','','','','','','','',''])
            wr.writerow(['Número','positive','negative','false positive','false negative','accuracy','precision','recall','true_negative'])
        wr.writerow([int(row['number']),int(row['positive']),int(row['negative']),int(row['false_positive']),int(row['false_negative']),float(row['result']['accuracy']),row['result']['precision'],row['result']['recall'],row['result']['true_negative']])
        i+=1
    myfile.close()
