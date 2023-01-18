#la méthode de LU 

import numpy as np

def E(i,j,x,dim):
    e=np.eye(dim)
    e[i][j]=x
    return e

def calcul_sous_det(A):
    n=len(A)
    for i in range(1,n+1) :
        if  np.linalg.det(A[:i,:i])!=0 : 
            return True
    return False


def LU(A):
    n=len(A)
    L=np.eye(n)
    if(calcul_sous_det(A)):
        for i in range(n-1):
            for j in range(i+1,n):
                e=E(j,i,-A[j][i]/A[i][i],n)
                L=np.matmul(L,np.linalg.inv(e))
                A=np.matmul(e,A)
        return (L,A)
    else :
        print("la matrice A ne peut pas etre decomposer en LU")


def res_LU(A,B):
    L,U=LU(A)
    Y=(np. linalg. inv(L))@(B) 
    x=(np.linalg.inv(U))@(Y)
    return(x)

A=np.array([[2,1,3],[4,5,1],[3,0,2]])
(p1,p2)=LU(A)
print("\t -la matrice L est trangulaire inférieure à diagonale unité\n",p1)
print("\t -la matrice U est triangulaire supérieure \n",p2)
print("la matrice A est \n",np.matmul(p1,p2))
B=np.array([1,2,3])
print("\n \t --la résolution de l'équation AX=B donne comme solution X \n ")
print(res_LU(A,B))
