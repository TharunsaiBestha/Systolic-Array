import numpy as np
path="/home/eee/Documents/C++/Matrix/"
def matrix_to_systolic_matrix(A):
    row=len(A)
    col=len(A[0])
    a=row-1
    b=0
    res=[]
    for i in range(0,row):
        res.append([0]*a+A[i]+[0]*b)
        a=a-1
        b=b+1
    return res
def random_matrix(low,high,size_t):
    temp=np.random.randint(low,high,size=size_t)
    return temp.tolist()
def genAB(low,high,size):
    A=random_matrix(low,high,size)
    B=random_matrix(low,high,size)
    A=matrix_to_systolic_matrix(A)
    B=matrix_to_systolic_matrix(B)
    B=np.array(B).T.tolist()
    return (A,B)
def to_file(A,B):
    rowA=len(A)
    colA=len(A[0])
    pathA=path+"A.txt"
    Fa=open(pathA,"w")
    for i in range(colA-1,-1,-1):
        for j in range(0,rowA):
            temp='{:032b}'.format(A[j][i])
            Fa.write(temp+"\n")
    Fa.close()
    rowB=len(B)
    colB=len(B[0])
    Fb=open(path+"B.txt","w")
    for i in range(rowB-1,-1,-1):
        for j in range(0,colB):
            temp='{:032b}'.format(B[i][j])
            Fb.write(temp+"\n")
    Fb.close()
            
            
            
    
    