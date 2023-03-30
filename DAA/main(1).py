import numpy as np
 
def max(a,b,c):
    if(a>b):
        if(a>c): return a;
        else: return c;
    
    else:
        if(b>c): return b;
        else: return c;
        
np.random.seed(42)
s1 = np.random.choice(['A', 'T', 'G', 'C'], 50)
s2 = np.random.choice(['A', 'T', 'G', 'C'], 50)

match_score = 5
mismatch_score = -4

l1 = len(s1)
l2 = len(s2)

align_mat[l2+1][l1+1]

for i in range(0,len(l2+1)):
    alignment_matrix[0][i] = 0;
        
        
for j in range(0,len(l1+1)):
    alignment_matrix[j][0] = 0;
    
for i in range(0,len(l2+1)):          
    for j in range(0,len(l1+1)):
        
        if(s1[j-1] == s2[i-1]):
            alignment_matrix[i][j] = alignment_matrix[i-1][j-1] +match_score;
        else:
            alignment_matrix[i][j] = maximum_element(alignment_matrix[i-1][j],alignment_matrix[i][j-1],alignment_matrix[i-1][j]-1)+mismatch_score;
        
    if(alignment_matrix[i][j] > max_score):
        max_score = alignment_matrix[i][j]
        max_i = i
        max_j = j

    
i = max_i;
j = max_j;
    
while i!=0 and j!=0 :
    if(s1[j-1] == s2[i-1]):
        print(s1[j-1]+'\t'+s2[i-1])
        i -= 1;
        j -= 1;
        
    else:
        if(alignment_matrix[i-1][j] > alignment_matrix[i][j-1] and alignment_matrix[i-1][j] > alignment_matrix[i-1][j-1]):
            print('_' + '\t' + s2[i-1])
            i-= 1
            
        
        elif(alignment_matrix[i][j-1] > alignment_matrix[i-1][j] and alignment_matrix[i][j-1] > alignment_matrix[i-1][j-1]):
            print(s1[j-1]+'\t'+'_');
            j-= 1
        
    

print("Max i: "+max_i+'/n'+"Max j: "+max_j);
    
for i in range(0,len(l2+1)):
    for j in range(0,len(l1+1)):
        print(alignment_matrix[i][j]+'\t')
        
    print('/n')    
    
    
    
    