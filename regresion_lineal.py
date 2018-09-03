import numpy as np #Importamos la utileria de Numpy
import matplotlib #I,portamos la matplotlib para poder graficar
import tkinter #Inportamos tkinter para poder user librerias de tk que se usan Linux con gnome y kde
from numpy import ones,linalg,array,corrcoef
from pylab import plot,show

#Cargamos el archivo en una arreglo de numpy y solo usamos las columnas de de distancia y litros
a = np.loadtxt("/home/cgg/Practicas/distanciaCombustible.csv", delimiter=",", skiprows=1, usecols=[2, 3])

distancia = np.array(a[:,0]) #Asiganos los valores de distancia a un arreglo de numpy
litros = np.array(a[:,1]) #Asignamos los valores de litros a un arreglo de numpy

rendimietno = litros/distancia #Calculamos el rendimiento

A = array([ distancia, ones(len(distancia))]) #Creamos un nuevo arreglo con la combinacion de unos y distancia

y = litros

#Calculamos la transpuesta de A
print (A.T)
#Obtenemos los parametros para calcular la regresion con la trasnpuesta de A
w = linalg.lstsq(A.T,y,rcond = None)[0] #Ponemos la condicion rcond para evitar warnings
print (w) #Coeficientes

#Calculamos la regresion lineal
linea = (w[0]*distancia+w[1])
print(linea)

#Obtenemos la catidad de litros que se requieren para recorrer 100,200,500 Kilometros
print("Litros para recorrer 100Km: ", w[0]*100+w[1])
print("Litros para recorrer 200Km: ", w[0]*200+w[1])
print("Litros para recorrer 500Km: ", w[0]*300+w[1])

#Calculamos la distancia con 200 litros
print ("Distancia aproximada con 200 litros: ", (200-w[1]/w[0]))

#Calculamos el coeficiente de correlacion de las variables
print("Coeficiente de relacion: ", corrcoef(distancia.tolist(), litros.tolist())[1,0])

#Graficamos los resultados
plot(distancia,linea,'r-',distancia,y,'o', markersize=.5)
show()
