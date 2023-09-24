# Algoritmo que reciba una cantidad de números y devuelve el promedio de 
# los valores ingresados

from clases import Operaciones

promedio=Operaciones() 
promedio.agregar_numeros()
print("Los números ingresados son: ")
promedio.mostrar_numeros()
print("El promedio es: ")
print(promedio.promedio())





