import sys, csv

from MLP import *

if __name__ == "__main__":
    
    mlp_config = Configuration()
    
    # read the argv to get commands
    commands = sys.argv[1:len(sys.argv)]
    for i in range(len(commands)):
        commands[i] = commands[i].lower()
        
    if '-e' in commands:
        t_index = commands.index('-e')
        mlp_config.iterations = int(commands[t_index+1])
    
    if '-b' in commands:
        t_index = commands.index('-b')
        mlp_config.num_bias = int(commands[t_index+1])
    
    if '-i' in commands:
        t_index = commands.index('-i')
        mlp_config.num_input_layer = int(commands[t_index+1])
        
    if '-h' in commands:
        t_index = commands.index('-h')
        mlp_config.num_hidden_layer = int(commands[t_index+1])
        
    if '-o' in commands:
        t_index = commands.index('-o')
        mlp_config.num_output_layer = int(commands[t_index+1])
    
    if '-l' in commands:
        t_index = commands.index('-l')
        mlp_config.learning_rate = float(commands[t_index+1])
    
    if '-f' in commands:
        t_index = commands.index('-f')
        mlp_config.boost_factor = float(commands[t_index+1])
    
    # create a default 
    #   multiple layer perceptron
    mlp = MLP()
    
    # open the file to trainning
    #   the mlp
    with open(mlp_config.file_trainning,'rb') as f:
        reader = csv.reader(f)
        cvs_train_rows = map(tuple,reader)
    size_matrix = len(cvs_train_rows)
    print size_matrix,' examples to train'
    
    
    training = []
    #training = [
    #    [[0,0], [0]],
    #    [[0,1], [1]],
    #    [[1,0], [1]]
    #]
    num_rows = 0
    for row in cvs_train_rows:
        number = []
        number.append(int(row[0]))
        matrix = row[1:len(row)-1]
        num_rows = len(matrix)
        matrixToSend = []
        for collum in matrix:
            matrixToSend.append(int(collum))
        training.append([matrixToSend,number])
    print num_rows,' rows'
    mlp.train(training)
    
    
    # open the file with examples
    #   to test the mlp
    with open(mlp_config.file_test,'rb') as f:
        reader = csv.reader(f)
        cvs_test_rows = map(tuple,reader)
    size_matrix = len(cvs_test_rows)
    print size_matrix,' examples to test'
    
    
    test = []
    #test = [
    #    [[0,0], [0]],
    #    [[0,1], [1]],
    #    [[1,0], [1]],
    #    [[1,1], [0]]
    #]
    for row in cvs_test_rows:
        number = []
        number.append(int(row[0]))
        matrix = row[1:len(row)-1]
        matrixToSend = []
        for collum in matrix:
            matrixToSend.append(int(collum))
        test.append([matrixToSend,number])
    mlp.test(test)
    mlp.print_weights()

    #mlp.test(training)
    #mlp.print_weights()
    