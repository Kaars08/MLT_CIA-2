# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:48:05 2023

@author: karu0
"""
#%% Basics
inputs = [[1.2,5.1,2.1],
          [2,5,-6],
          [3.5,-6,7.8]] #vector features from a single sample  now separated as badges

weights1 = [[3.1,2.1,8.7],
           [0.5,0.9,0.2],
           [0.2,0.1,0.8]] #vector

biases1 = [2,3,0] #vector

weights2 = [[3,0.2,8.7],
           [1.5,2.9,0.2],
           [0.2,6.1,0.8]] #vector

biases2 = [2,3.8,0.5] #vector

import numpy as np


layer1_output = np.dot(weights1,inputs)+biases1
layer2_output = np.dot(weights2,layer1_output)+biases2

print(layer1_output,'\n')
print(layer2_output)

#%% Objects
X = [[1.2,5.1,2.1],
          [2,5,-6],
          [3.5,-6,7.8]]

import nnfs
from nnfs.datasets import spiral_data
nnfs.init()
 
X,y = spiral_data(100, 3)

class layer_dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.10*np.random.randn(n_inputs,n_neurons) #actual shape
        self.bias = np.zeros((1,n_neurons)) #actual shape in tuple
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.bias
        
#%% Activation Functions
#RElu - rectified linear unit if y<x --> y=0; y>x -->y=x
class activation_layer_RElu:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)
 
    
 
layer1 = layer_dense(2,3)
activation1 = activation_layer_RElu()
layer1.forward(X)
activation1.forward(layer1.output)

print(layer1.output,'\n')
print(activation1.output)
#%% SoftMax Activation Function
class Activation_softmax:
    def forward(self,input):
        exp_val = np.exp(inputs - np.max(inputs,axis = 1,keepdims = True))
        prob = exp_val/np.sum(exp_val,axis = 1,keepdims = True)
        self.output = prob
        
X,y = spiral_data(100,3)

dense2 = layer_dense(3,3)
activation2 = Activation_softmax()

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(dense2.output)
print(activation2.output)
#%% Loss  Function
class Loss:
    def calculate(self,output,y):
        sample_loss = self.forward(output,y)
        data_loss = np.mean(sample_loss) 
        return data_loss
class loss_categ(Loss):
    def forward(self,y_pred,y_true):
        samp = len(y_pred)
        y_pred_clipped = np.clip(y_pred,1e-7,1-1e-7)
        
        if(len(y_true.shape)==1):
            correct_confidence = y_pred_clipped[range(samp),y_true]
        elif(len(y_true.shape)==2):
            correct_confidence = np.sum(y_pred_clipped*y_true,axis =1)
               
        neg_log_like = -np.log(correct_confidence)
        return neg_log_like

loss_func = loss_categ()
loss = loss_func.calculate(activation2.output,y)

print("loss:",loss)

 


 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    