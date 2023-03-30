# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:15:08 2023

@author: karunya Harikrishnan
"""
#%% Generating Random sequences
import numpy as np
np.random.seed(92)
s1 = np.random.choice(['A', 'T', 'G', 'C'], 16)
s2 = np.random.choice(['A', 'T', 'G', 'C'], 16)
#%% populating matrix with and without recursion
l1 = len(s1)
l2 = len(s2)

mat = [[0 for i in range(l1+1)]for
       j in range(l2+1)]

def print_mat(mat,l1,l2):
    print('[',end = " ")
    for i in range(0,l1+1):
        for j in range(0,l2+1):
            print(mat[i][j],end = " ")
        print('\n')
    print(']')
       
def populating(mat,s1,s2,l1,l2):
    match = 5
    mismatch = -4
    max_ele = 1
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if(s1[i-1]==s2[j-1]):
                mat[i][j] = mat[i-1][j-1]+match
            else:
                mat[i][j] = max(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])+ mismatch
            if(mat[i][j] > max_ele):
                max_ele = mat[i][j]
                max_i = i
                max_j = j
    return max_i,max_j

max_i,max_j = populating(mat,s1,s2,l1,l2)               
print('max element at: ',max_i,max_j )
print('Populating without recursion:')
print_mat(mat,l1,l2)

def rec_populating(i,j,s1,s2,mat):
    match = 5
    mismatch = -4
    if(s1[i-1] == s2[j-1]):
        mat[i][j] = mat[i-1][j-1]+match
    else:
        mat[i][j] = max(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])+ mismatch 
        
    if i<len(s1): 
        rec_populating(i+1,j,s1,s2,mat)
    else:
        if j<len(s2):
            rec_populating(1,j+1,s1,s2,mat)
        else:
            return  

rec_populating(1,1,s1,s2,mat)
print('Populating with recursion:')
print_mat(mat,l1,l2)
print('\n')
#%% Backtracking recursively
def max_ele(mat,i,j):
    if(mat[i-1][j-1] > mat[i][j-1]):
        if(mat[i-1][j-1] > mat[i-1][j]):
            return i-1,j-1,mat[i-1][j-1]
        else:
            return i-1,j,mat[i-1][j]
    else:
        if(mat[i][j-1] > mat[i-1][j]):
            return i,j-1,mat[i][j-1]
        else: 
            return i-1,j,mat[i-1][j]
        
def rec_backtrack(mat,i,j):
    curr_i,curr_j,next_ele = max_ele(mat,i,j)
    print(next_ele,'--',end = " ")
    if(mat[curr_i][curr_j] != 0):
        rec_backtrack(mat,curr_i,curr_j)
    else:
        return 
    
print('Backtracking(done recursively):') 
rec_backtrack(mat,max_i,max_j)       
print('\n')  
#%%
def gaps(s1,s2,mat,i,j):
    while((i!=0 and j!=0)):
        if(s1[j-1] == s2[i-1]):
            print(s1[j-1],'\t',s2[i-1])
            i -= 1
            j -= 1
        
        
        else:
            if(mat[i-1][j] > mat[i][j-1] and mat[i-1][j] > mat[i-1][j-1]):
                print('here')
                print('_' ,'\t',s2[i-1])
                i-=1
            
        
            elif(mat[i][j-1] > mat[i-1][j] and mat[i][j-1] > mat[i-1][j-1]):
                print('her')
                print(s1[j-1],'\t','_')
                j-=1
            '''elif(mat[i-1][j-1] > mat[i-1][j] and mat[i-1][j-1] > mat[i][j-1]):
                print(s1[j],'\t','_')'''
            
        
gaps(s1,s2,mat,max_i,max_j)







