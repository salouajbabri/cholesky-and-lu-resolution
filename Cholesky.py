def cholesky(A): 
    n=len(A)
    if(is_pos_def(A)):
      L=np.array([[0]*n]*n)
      L[0][0]=(A[0][0])**1/2
      for j in range(1,n):
          L[j][0]=A[j][0]/L[0][0]
      for i in range(1,n):
          L[i][i]=(A[i][i]-sum((L[i][k])**2 for k in range(0,i)))**(1/2)
          for j in range(i+1,n):
              L[j][i]=A[i][j]-sum(L[j][k]*L[i][k] for k in range(0,i))
              L[j][i]=L[j][i]/L[i][i]
      return L 
    else :
      print("\t\t <-- la matrice n'est pas définie positive --> ")   


# Résolution de l'équation AX = B consiste à résoudre LY = B avec A =LL* et Y=L*X
def cholesky_leq(A,b) : 
    L=cholesky(A)
    Y=(np. linalg. inv(L))@(b) 
    x=(np.linalg.inv(L.transpose()))@(Y)
    return(x)

print("\t\t --> la matrice A vérifie la condition définie positive <-- \n")
print("\t\t -->> Voilà la décomposition de Cholesky <<-- \n ")
print("\t    La matrice L est triangulaire inférieure ")                 
A=np.array([[2,1,1],[1,2,1],[1,1,2]])
print(cholesky(A))
print("\t    La matrice L* est triangulaire supérieure ") 
print(cholesky(A).transpose())
B=np.array([1,2,3])
print("\t--la solution X est \n")
print(cholesky_leq(A,B))
