import numpy as np
import math

print("\n")
print("------- CIFRA DE PLAYFAIR -------")
print("\n")
print("Menu de Opcoes:")
print("\n")
print("1 - Cifrar Mensagem")
print("\n")
print("2 - Decifrar Mensagem")
print("\n")
print("0 - Terminar")
print("\n")

Opcao=int(input("Informe sua Opcao: "))

def verifica(a,b):
    c=False
    for k in range(5):
        for l in range(5):
            if ord(a[k][l]) == ord(b):
                c = True
    return c

def posicion(a,b):
    pos="00"
    for i in range(5):
        for j in range(5):
            if ord(a[i][j])==ord(b):
                pos=str(i)+""+str(j)
    return pos
def construir_matriz(deixar,Chave):
    Alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    cont = 0
    cont2 = 0
   
    for i in range(5):
        for j in range(5):
            while True:
                if cont < len(Chave):
                    if not verifica(deixar, Chave[cont]):
                        deixar[i][j] = Chave[cont]
                        cont = cont + 1
                        break
                    else:
                        cont = cont + 1
                else:
                    while True:
                        if cont2 < len(Alfabeto):
                            if not verifica(deixar, Alfabeto[cont2]):
                                deixar[i][j] = Alfabeto[cont2]
                                cont2 = cont2 + 1
                                break
                            else:
                                cont2 = cont2 + 1
                    break

    print("Resultado de Matriz")
    for i in range(5):
        for j in range(5):
            if deixar[i][j] == b'I':
                print('I/J', " ", end='')
            else:
                print(deixar[i][j].decode(), "\t", end='')
        print("")

    print("\n")
    return deixar

if Opcao==1:
    Texto = input("Por favor, digite o texto para cifrar: ")
    Chave = input("Por favor insira a chave: ")
    
    Texto = Texto.upper().strip().replace(" ", "")
    Texto = Texto.replace("J", "I")
    
    Chave = Chave.upper().strip().replace(" ", "")
    Chave = Chave.replace("J", "I")

    deixar = np.chararray((5, 5))
    deixar[:] = '*'
    deixar=construir_matriz(deixar,Chave)

    pares=np.chararray(((math.ceil(len(Texto)/2))+1,2))
    pares[:]='X'

    cifrado = np.chararray(((math.ceil(len(Texto) / 2)) + 1, 2))
    cifrado[:] = 'X'

    cont=0
    for i in range (math.ceil(len(Texto)/2)+1):
        for j in range(2):
            if cont<len(Texto):
                pares[i][j] = Texto[cont]
                cont+=1
                if (j==1 and pares[i][0] != b'X' and pares[i][0]==pares[i][1]):
                    pares[i][1]=b'X'
                    cont-=1


    X1=0
    X2=0
    
    Y1=0
    Y2=0

    for i in range(math.ceil(len(Texto) / 2) + 1):
        for j in range(2):
            if (j == 0):
                X1 = posicion(deixar,pares[i][j])[0]
                X2 = posicion(deixar,pares[i][j])[1]
            else:
                Y1 = posicion(deixar,pares[i][j])[0]
                Y2 = posicion(deixar,pares[i][j])[1]
            
            X1 = int(X1)
            Y1 = int(Y1)
            X2 = int(X2)
            Y2 = int(Y2)
            
            W1=X1
            W2=Y2

            Z1=Y1
            Z2=X2
            
            if X2 == Y2:
                W2=X2
                Z2=Y2
                W1=X1+1
                Z1=Y1+1
                if W1==5:
                    W1=0
                if Z1==5:
                    Z1=0

            if X1 == Y1:
                W1 = X1
                Z1 = Y1
                W2 = X2 + 1
                Z2 = Y2 + 1
                if W2 == 5:
                    W2 = 0
                if Z2 == 5:
                    Z2 = 0

            cifrado[i][0] = deixar[W1][W2]
            cifrado[i][1] = deixar[Z1][Z2]

    print("TEXTO CIFRADO: ")
    for i in range (math.ceil(len(Texto)/2)+1):
        for j in range(2):
            print(cifrado[i][j].decode(), end='')
    
if Opcao==2 :
    Texto = input("Por favor, digite o texto para decifrar: ")
    Chave = input("Por favor insira a chave: ")
    
    Texto = Texto.upper().strip().replace(" ", "")
   
    Chave = Chave.upper().strip().replace(" ", "")
    Chave = Chave.replace("J", "I")

    deixar = np.chararray((5, 5))
    deixar[:] = '*'
    deixar = construir_matriz(deixar, Chave)

    pares=np.chararray(((math.ceil(len(Texto)/2))+1,2))
    pares[:]='X'

    descifrado = np.chararray(((math.ceil(len(Texto) / 2)) + 1, 2))
    descifrado[:] = 'X'

    cont=0
    for i in range (math.ceil(len(Texto)/2)):
        for j in range(2):
            if cont<len(Texto):
                pares[i][j] = Texto[cont]
                cont+=1
                if (j==1 and pares[i][0] != b'X' and pares[i][0]==pares[i][1]):
                    pares[i][1]=b'X'
                    cont-=1


    W1=0
    W2=0
   
    Z1=0
    Z2=0

    for i in range(math.ceil(len(Texto) / 2)):
        for j in range(2):
            if (j == 0):
                W1 = posicion(deixar,pares[i][j])[0]
                W2 = posicion(deixar,pares[i][j])[1]
            else:
                Z1 = posicion(deixar,pares[i][j])[0]
                Z2 = posicion(deixar,pares[i][j])[1]
       
            W1 = int(W1)
            Z1 = int(Z1)
            W2 = int(W2)
            Z2 = int(Z2)

            
            X1=W1
            X2=Z2

            Y1=Z1
            Y2=W2
            
            if W2 == Z2:
                X2=W2
                Y2=Z2
                X1=W1-1
                Y1=Z1-1
                if X1==5:
                    X1=0
                if Y1==5:
                    Y1=0
                if X1 == -1:
                    X1 = 4
                if Y1 == -1:
                    Y1 = 4

            if W1 == Z1:
                X1 = W1
                Y1 = Z1
                X2 = W2 - 1
                Y2 = Z2 - 1
                if X2 == 5:
                    X2 = 0
                if Y2 == 5:
                    Y2 = 0

                if X2 == -1:
                    X2 = 4
                if Y2 == -1:
                    Y2 = 4

            descifrado[i][0] = deixar[X1][X2]
            descifrado[i][1] = deixar[Y1][Y2]

    print("TEXTO DECIFRADO: ")
    for i in range (math.ceil(len(Texto)/2)):
        for j in range(2):
            print(descifrado[i][j].decode(), end='')

if Opcao==0 :
  print("exit()")
