import numpy as np
import re
import arff
b1= open('lp1.data',"r").read()
b2= open('lp2.data',"r").read()
b3= open('lp3.data',"r").read()
b4= open('lp4.data',"r").read()
b5= open('lp5.data',"r").read()

matriz = b1+b2+b3+b4+b5
atributos = []
for i in range(6):
    for j in range(15):
        if i + 1  == 1:
            atributos.append('Fx' + str(j+1))
        if  i + 1 == 2:
            atributos.append('Fy' + str(j+1))
        if  i + 1 == 3:
            atributos.append('Fz' + str(j+1))
        if  i + 1 == 4:
            atributos.append('Tx' + str(j+1))
        if  i + 1 == 5:
            atributos.append('Ty' + str(j+1))
        if  i + 1 == 6:
            atributos.append('Tz' + str(j+1))
print(atributos)

clases = ['normal','collision','fr_collision','front collision','obstruction','back collision','collision to the right','collision to the left','ok','slightly moved','moved','lost','bottom collision','bottom obstruction','collision in part','collision in tool']

NoEspacios = b1.split()
renglonSinOrdenar = []
matrizSinOrdenar = []

#print(len(NoEspacios))


i = 0
for registro in NoEspacios:
    if i < 90:
        renglonSinOrdenar.append(registro)
        #print (registro)
        i = i + 1
    else:
        renglonSinOrdenar.append(registro)
        matrizSinOrdenar.append(renglonSinOrdenar)
        renglonSinOrdenar = []
        i = 0
#print(matrizSinOrdenar)

errorActual = ''
numRegistro = 0
matrizOrdenada = []
numRenglon = 1
numColumnas = 6

matriz = []
renglon_matriz = []
numRegistro = 1
matrices = []
clasesCapturadas = []

for renglon in matrizSinOrdenar:
    #print(len(renglon))
    renglon_matriz= []
    numRegistro = 1
    for registro in renglon:
        if registro in clases:
            errorActual = registro
            clasesCapturadas.append(registro)
        else:
            if numRegistro < numColumnas+1:
                #print(registro)
                renglon_matriz.append(float(registro))
            else:
                renglon_matriz.append(float(registro))
                numRegistro = 1
                matriz.append(renglon_matriz)
                renglon_matriz= []
                    
        numRegistro = numRegistro + 1
    numRenglon = numRenglon + 1
    matrices.append(np.array(matriz).transpose())
    matriz = []
#print(matrices)

#print(len(matrices))
# matrizOrdenada = np.array(matriz).transpose()

# print(matrizOrdenada)

cont = 0
a = []
data = []
for m in matrices:
    a = np.ravel(m).tolist()
    a.append(clasesCapturadas[cont])
    print(a)
    print('--------------------------------------------------------------------------------------------------------------')
    data.append(a)
    cont = cont + 1


arff.dump('Resultado.arff', data, relation="Errores", names= atributos)