#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
import keras

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.optimizers import RMSprop
from keras.utils import np_utils
from keras import backend as K

class Configuration:
    model           = None
    batch_size      = None
    nb_classes      = None
    nb_epoch        = None
    file_trainning  = None
    file_test       = None
    num_cols        = None
    num_rows        = None    
    
    def __init__(self, model='sequential', batch_size=128, nb_classes=10, nb_epoch=15, file_trainning='data/mnist_train.csv', file_test='data/mnist_test.csv', num_cols=28, num_rows=28):
        self.model          = model
        self.batch_size     = batch_size
        self.nb_classes     = nb_classes
        self.nb_epoch       = nb_epoch
        self.file_trainning = file_trainning
        self.file_test      = file_test
        self.num_cols       = num_cols
        self.num_rows       = num_rows
    
class Keras:
    config      = None
    
    model       = None
    
    x_labels    = None
    y_labels    = None
    X_train     = None
    y_train     = None
    X_test      = None
    y_test      = None
    
    def __init__(self):
        
        self.config     = Configuration()
        
        if self.config.model == 'sequential':
            self.model = Sequential()
        else:
            self.model = Sequential()
            
    def run_mlp(self):
        
        train           = pd.read_csv(self.config.file_trainning)
        test            = pd.read_csv(self.config.file_test)
        
        # y_train and y_test => set of date
        self.y_train    = train.ix[:,0].values.astype('float64')
        self.y_test     = test.ix[:,0].values.astype('float64')
        
        # X_train an X_test => set of labels
        self.X_train    = (train.ix[:,1:].values).astype('float64')
        self.X_test     = (test.ix[:,1:].values).astype('float64')
        
        
        # change list of labels to categorial list
        self.Y_train    = np_utils.to_categorical(self.X_train)
        self.Y_test     = np_utils.to_categorical(self.X_test)
        
        # Find the max and subtract the mean
        scale           = np.max(self.X_train)
        self.X_train   /= scale
        self.Y_test    /= scale
        
        mean = np.std(self.X_train)
        self.X_train    -= mean
        self.X_test     -= mean
        
        print(self.X_train.shape[0], 'train samples')
        print(self.X_test.shape[0], 'test samples')
        
        
        input_shape = (img_rows, img_cols, 1)
        
        self.Y_train = np_utils.to_categorical(self.y_train, self.config.nb_classes)
        self.Y_test = np_utils.to_categorical(self.y_test, self.config.nb_classes)
        
        self.model = Sequential()    
        
        self.model.add(Dense(512, input_shape=(784,)))
        self.model.add(Activation('relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(512))
        self.model.add(Activation('relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(10))
        self.model.add(Activation('softmax'))
        
        self.model.summary()

        self.model.compile(loss='categorical_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])

        history = self.model.fit( self.X_train, self.Y_train, batch_size=self.config.batch_size, nb_epoch=self.config.nb_epoch, verbose=1, validation_data=(self.X_test, self.Y_test))
        score = self.model.evaluate(self.X_test, self.Y_test, verbose=0)
        print('Test score:', score[0])
        print('Test accuracy:', score[1])
        
            
    def run(self):
    
        
        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()
        
        if K.image_data_format() == 'channels_first':
            self.X_train = self.X_train.reshape(self.X_train.shape[0], 1, self.config.num_rows, self.config.num_cols)
            self.X_test = self.X_test.reshape(self.X_test.shape[0], 1, self.config.num_rows, self.config.num_cols)
            input_shape = (1, self.config.num_rows, self.config.num_cols)
        else:
            self.X_train = self.X_train.reshape(self.X_train.shape[0], self.config.num_rows, self.config.num_cols, 1)
            self.X_test = self.X_test.reshape(self.X_test.shape[0], self.config.num_rows, self.config.num_cols, 1)
            input_shape = (self.config.num_rows, self.config.num_cols, 1)
    
        
        self.Y_train = keras.utils.to_categorical(self.y_train, self.config.nb_classes)
        self.Y_test = keras.utils.to_categorical(self.y_test, self.config.nb_classes)
        
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=(5, 5), activation='relu', input_shape=input_shape))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.3))
        self.model.add(Conv2D(64, kernel_size=(4, 4), activation='relu', input_shape=input_shape))
        self.model.add(Conv2D(34, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.3))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(self.config.nb_classes, activation='softmax'))
        
        self.model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

        self.model.summary()
        history = self.model.fit( self.X_train, self.Y_train, batch_size=self.config.batch_size, nb_epoch=self.config.nb_epoch, verbose=1, validation_data=(self.X_test, self.Y_test))
        score = self.model.evaluate(self.X_test, self.Y_test, verbose=0)
        print('Test score:', score[0])
        print('Test accuracy:', score[1])
