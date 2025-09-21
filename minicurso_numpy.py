import numpy as np

# crear un array e imprimir sus valores y tamaño
mylist = [1, 2, 3]
myarray = np.array(mylist)
print(myarray)
print(myarray.shape)

# Hacer una matriz de 2x3 e imprimir la primea y ultima lista
# luego imprimir un elemento en concreto y los valores de la tercera columna 
mylist =[[1,2,3], [4,5,6]]
myarray = np.array(mylist)
print(f"primera fila {myarray[0]}")
print(f"Ultima fila {myarray[-1]}")
print(f"Elemento fila 1 columna 1 : {myarray[1,0]}")
print(f"Elementos de la columna 3 {myarray[ : ,2]}") #  : , 2 todas las filas de la columna 3

# crear dos vectores y sumarlos y mutiplicarlos
myarray1 = np.array([2, 2, 2, 2])
myarray2 = np.array([3, 3, 3, 3])
print(f"Suma {myarray1 + myarray2}")
print(f"Multiplicacion {myarray1 * myarray2}")