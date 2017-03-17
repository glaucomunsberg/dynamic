# A MultiLayer Perceptron (MLP)
    
A simple implementation of multilayer perceptron. Coded and run with Python >= 2.7

#### Run

`$ python MLP_test.py [-e|-b|-i|-h|-o INT] [-l|-f FLOAT] `

Attribute | Description
--------- | -----------
`-e INT`  | Eras ou Interations
`-b INT`  | number of bias
`-i INT`  | Number of input layers
`-h INT`  | Number of hidden layers
`-o INT`  | Number of output layers
`-l FLOAT`| Learning Rate
`-f FLOAT`| Boost Factor

#### Config

You always can change the configuration on the Configuration.py


Attribute         | Default value             | Description
----------------- | ------------------------- | -------------
input_weight_min  | -0.2                      | Min value to set the input weight
input_weight_max  | 0.2                       | Max value to set the input weight
output_weight_min | -2.0                      | Min value to set the output weight
output_weight_max | 2.0                       | Min value to set the input weight
num_input_layer   | 2                         | Number of perceptrons on initial layer
num_hidden_layer  | 2                         | Number of perceptrons on intermediary(hidden) layer
num_output_layer  | 1                         | Number of perceptrons on out layer
num_bias          | 1                         | Number of bias
iterations        | 1000                      | Number of iterarions (eras)
learning_rate     | 0.3                       | Learning rate usade
boost_factor      | 0.1                       | Momentum factor

#### Notes

> Only one layer hidden is avaliable