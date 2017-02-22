# -*- coding: utf-8 -*-
from random import choice
from numpy import array, dot, random
from Perceptron import Perceptron
from Mongo import Mongo

import pymongo, datetime,bson,time
import time
import csv

if __name__ == "__main__":

    start = time.time()
    border      = 5 # scale of gray that is considered black
    unit_step   = lambda x: 0 if x < 0 else 1
    mongo = Mongo()

    training_data = [
        (array([0,0,1]), 0),
        (array([0,1,1]), 1),
        (array([1,0,1]), 1),
        (array([1,1,1]), 1),
    ]
    test_data = array([0,0,1])

    print 'Creating perceptrons...'
    results = []
    perceptrons = []
    for i in range(10):
        print 'Creating perceptron to number',i
        perceptrons.append(Perceptron(100,783))
        results.append({})
        results[i]['time']             = 0
        results[i]['number']           = i
        results[i]['positive']         = 0
        results[i]['negative']         = 0
        results[i]['false_positive']   = 0
        results[i]['false_negative']   = 0

    print 'Loading train file...'
    with open('data/mnist_train.csv', 'rb') as f:
        reader = csv.reader(f)
        cvs_train_rows = map(tuple, reader)
    size_matrix = len(cvs_train_rows)
    print size_matrix,' lines'

    print 'Training...'
    for row in cvs_train_rows:
        number = int(row[0])
        matrix = row[1:len(row)-1]
        #print 'Matrix',matrix
        matrixToSend = []
        for collum in matrix:
            matrixToSend.append(int(collum))
        #print 'Matrix to send',matrixToSend
        for i in range(len(perceptrons)):
            expected = 0
            if i == number:
                expected = 1
            toSend = [
                (array(matrixToSend), expected)
            ]
            perceptrons[i].training_data(toSend)

    with open('data/mnist_test.csv', 'rb') as f:
        reader = csv.reader(f)
        cvs_test_rows = map(tuple, reader)

    print len(cvs_test_rows),' lines'
    for row in cvs_test_rows:
        number = int(row[0])
        matrix = row[1:len(row)-1]
        matrixToSend = []
        results[number]['time'] += 1
        for collum in matrix:
            matrixToSend.append(int(collum))
        for i in range(len(perceptrons)):
            expected = 0
            if i == number:
                expected = 1
            toSend = array(matrixToSend)
            boolean_return = perceptrons[i].test_data_boolean(toSend)
            # print 'number',number,'perceptron',i,'expected',expected,'boolean returned',boolean_return

            if expected == 1 and boolean_return == 1:
                results[number]['positive'] += 1
                #print 'POSITIVO'
            elif expected == 0 and boolean_return == 1:
                results[number]['false_positive'] += 1
                #print 'FALSOPOSITIVO'
            elif expected == 1 and boolean_return == 0:
                results[number]['false_negative'] += 1
                #print 'FALSONEGATIVO'
            else:
                results[number]['negative'] += 1
                #print 'NEGATIVO'

    for result in results:
        print 'number',result['number']
        result['weights']                 = {}
        result['weights']                 = perceptrons[result['number']].getWeight()
        result['result']                  = {}
        result['result']['accuracy']      = (result['positive']+result['negative'])/float(10*result['time'])
        result['result']['precision']     = result['positive'] / float(result['positive']+result['false_positive'])
        result['result']['recall']        = result['positive'] / float(result['positive']+result['false_negative'])
        result['result']['true_negative'] = result['negative'] / float(result['negative']+result['false_positive'])
        #result['result']['f_medida']      = (result['result']['precision']*result['result']['recall'])/float(result['result']['precision']+result['result']['recall'])
        print result
        print ''

    mongo.insertResults(results)


    #perceptron.training_data(training_data)
    #print("data {} -> {}".format(test_data,perceptron.test_data_boolean(test_data)))
    #print("data {} -> {}".format(training_data[2][0],perceptron.test_data_boolean(training_data[2][0])))

    end = time.time()

    elapsed = end - start
    print 'End after',elapsed,'seconds'
