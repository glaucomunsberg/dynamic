#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, random, string, datetime

class Configuration:
    _instance           = None
    
    input_weight_min    = None
    input_weight_max    = None
    output_weight_min   = None
    output_weight_max   = None
    num_input_layer     = None
    num_hidden_layer    = None
    num_output_layer    = None
    num_bias            = None
    interations         = None  # eras
    file_trainning      = None
    file_test           = None
    
    def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
		return cls._instance
    
    def __init__(self):
        self.input_weight_min   = -0.2
        self.input_weight_max   = 0.2
        self.output_weight_min  = -2.0
        self.output_weight_max  = 2.0
        self.num_input_layer    = 783#2
        self.num_hidden_layer   = 783
        self.num_output_layer   = 1
        self.num_bias           = 1         # for bias 
        self.iterations         = 200#1000
        self.learning_rate      = 0.3
        self.boost_factor       = 0.1
        self.file_trainning     = 'data/fast_mnist_train.csv'
        self.file_test          = 'data/fast_mnist_test.csv'
        

class MLP:
    
    _config         = None
    _input_layer    = None
    _hidden_layer   = None
    _output_layer   = None

    _input_weights  = None
    _output_weights = None
    
    _input_activations  = None
    _hidden_activations = None
    _output_activations = None
    
    _change_input   = None
    _change_output  = None
    
    def __init__(self):
        
        self._config        = Configuration()
        
        # set the configuration informations
        
        self._input_layer   = self._config.num_input_layer + self._config.num_bias
        self._hidden_layer  = self._config.num_hidden_layer
        self._output_layer  = self._config.num_output_layer
        
        # creating the weights matrix
        #   to be used
        self._input_weights     = MLP.matrixWeights(self._input_layer,self._hidden_layer)
        self._output_weights    = MLP.matrixWeights(self._hidden_layer,self._output_layer)
        
        # creating the array
        #   of activations layers
        self._input_activations     = [1.0] * self._input_layer
        self._hidden_activations    = [1.0] * self._hidden_layer
        self._output_activations    = [1.0] * self._output_layer
        
        # initialize with random values
        #   from configurations 
        for i in range(self._input_layer):
            for j in range(self._hidden_layer):
                self._input_weights[i][j] = MLP.randomBetween(self._config.input_weight_min,self._config.input_weight_max)
        for i in range(self._hidden_layer):
            for j in range(self._output_layer):
                self._output_weights[i][j] = MLP.randomBetween(self._config.output_weight_min,self._config.output_weight_max)
        
        # make the last boost     
        self._change_input  = MLP.matrixWeights(self._config.num_input_layer + self._config.num_bias, self._config.num_hidden_layer)
        self._change_output = MLP.matrixWeights(self._config.num_hidden_layer,self._config.num_output_layer)
    
    
    def train(self, patterns):
        print datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M:%S')
        print 'Trainning'
        for i in range(self._config.iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets)
            j = i+10
            date = datetime.datetime.now().time().strftime('%H:%M:%S')
            print '↻ ',date,'iteration %03d'%j,'with error ⇢ %-.5f' % error
                
    
    # update
    #   update the activations simple =]
    def update(self, inputs):
        if len(inputs) != self._input_layer - self._config.num_bias:
            raise ValueError('Wrong number of inputs. Expected '+str(self._input_layer - self._config.num_bias)+' gived '+str(len(inputs)) )

        # input activations
        for i in range(self._input_layer-1):
            self._input_activations[i] = inputs[i]

        # hidden activations
        for j in range(self._hidden_layer):
            sum = 0.0
            for i in range(self._input_layer):
                sum = sum + self._input_activations[i] * self._input_weights[i][j]
            self._hidden_activations[j] = MLP.sigmoid(sum)

        # output activations
        for i in range(self._output_layer):
            sum_p = 0.0
            for j in range(self._hidden_layer):
                sum_p = sum_p + self._hidden_activations[j] * self._output_weights[j][i]
            self._output_activations[i] = MLP.sigmoid(sum_p)

        return self._output_activations[:]
    
    # backPropagate
    #   recieve the targets: Call the error (out and hidden)
    #   update the weigths and return the error
    def backPropagate(self, targets):
        if len(targets) != self._output_layer:
            print 'targests',len(targets)
            print 'output_layer',self._output_layer
            raise ValueError('Ooops! lenght different of targets and target')

        # output error
        output_deltas = [0.0] * self._output_layer
        for i in range(self._output_layer):
            error               = targets[i]-self._output_activations[i]
            output_deltas[i]    = MLP.derivateSigmoid(self._output_activations[i]) * error

        # hidden error
        hidden_deltas = [0.0] * self._hidden_layer
        for i in range(self._hidden_layer):
            error = 0.0
            for j in range(self._output_layer):
                error = error + output_deltas[j]*self._output_weights[i][j]
            hidden_deltas[i] = MLP.derivateSigmoid(self._hidden_activations[i]) * error

        # update output weights
        for i in range(self._hidden_layer):
            for j in range(self._output_layer):
                change = output_deltas[j]*self._hidden_activations[i]
                self._output_weights[i][j] = self._output_weights[i][j] + (self._config.learning_rate*change) + (self._config.boost_factor * self._change_output[i][j])
                self._change_output[i][j] = change

        # update input weights
        for i in range(self._input_layer):
            for j in range(self._hidden_layer):
                change = hidden_deltas[j] * self._input_activations[i]
                self._input_weights[i][j] = self._input_weights[i][j] + self._config.learning_rate*change + self._config.boost_factor*self._change_input[i][j]
                self._change_input[i][j] = change

        # Cal error
        error = 0.0
        for i in range(len(targets)):
            subvalue = targets[i] - self._output_activations[i]
            error = error + 0.5*(subvalue)**2
        return error
    
    def print_weights(self):
        print 'Input weights'
        for i in range(self._input_layer):
            print self._input_weights[i]
        print '/nOutput weights' 
        for j in range(self._hidden_layer):
            print self._output_weights[j]
        print '/n'
        
    def test(self, patterns):
        print '\nTest'
        for p in patterns:
            print p[0], ' ➔ ', self.update(p[0])
    
    # matrixWeights
    #   create the matrix with default
    #   values
    @staticmethod
    def matrixWeights(i,j,default=0.0):
        matrix   = []
        for position in range(i):
            matrix.append([default]*j)
        return matrix
    
    # randomBetween
    #   calculate a random number
    #   between a_value and b_values
    @staticmethod
    def randomBetween(a_value,b_value):
        return (b_value-a_value)*random.random() + a_value
    
    # derivateSigmoid
    #   derivate sigmoid function
    @staticmethod
    def derivateSigmoid(x):
        # original
        # return 1.0 - x**2
        #alternative 1
        return 1.0 - math.tanh(x)**2
        #alternative 2
        #return 1. / (1 + math.exp(-x)) * (1  - 1. / (1 + math.exp(-x)))

    # sigmoid
    #   function alternative 1/(1+e^-x)
    @staticmethod
    def sigmoid(x):
        # sigmoid
        return math.tanh(x)
        # sigmoid alternative
        #return 1. / (1 + math.exp(-x))
        
    
        
        