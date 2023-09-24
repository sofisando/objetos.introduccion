class Auto:
    marca = "volvo"
    color= "un color"
    aceleracion= "40"
    cant_combustible= 10
    encendido= False

    def encender(self):
        self.encendido= True

#esto no hace nada, es un molde

miAuto = Auto()
#esto es instanciar un objeto de una clase

print(miAuto.marca)
#devuelve "volvo"

miAuto.marca = "citroen"
print(miAuto.marca)

