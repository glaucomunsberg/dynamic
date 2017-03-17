from numpy import array, dot, random

class Perceptron:
    _unit_step  = None
    _errors     = None
    _eta        = None
    _n          = None
    _weight     = None
    _tranned    = None

    def __init__(self,n=100,weights_size=3,eta=0.3):
        self._unit_step = lambda x: 0 if x < 0 else 1
        self._errors    = []
        self._eta       = eta
        self._n         = n
        self._weight    = random.rand(weights_size)
        self._tranned   = 0

    def training_data(self,data):
        #print 'Start training...'
        for i in range(self._n):
            for vector, expected in data:
                result = dot(self._weight, vector)
                error = expected - self._unit_step(result)
                self._errors.append(error)
                self._weight += self._eta * error * vector
        self._tranned += self._n
        #print 'End training...'

    def test_data_range(self,vector):
        result = dot(vector, self._weight)
        return result

    def test_data_boolean(self,vector):
        result = dot(vector, self._weight)
        return self._unit_step(result)

    def getWeight(self):
        return self._weight
    
    #def dot(self,weight,vector):
    #   sum( [vector[i][0]*weight[i] for i in range(len(weight))] )
