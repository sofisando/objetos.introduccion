class Operaciones:
    def __init__(self):
        self.numeros= [] 
        self.suma_total=0
        self.numeros_cuadrados=[]

    def agregar_numeros(self):  
        while True:
            num= int(input("Ingrese numeros, si desea salir ingrese 0: "))
            if num == 0:
                break
            else:
                self.numeros.append(num)

    def mostrar_numeros(self):
        print(self.numeros)

    def sumar_nums(self):
        if not self.numeros:
                return 0  # En caso de que no se hayan ingresado números
        self.suma_total = sum(self.numeros)
        return self.suma_total

    def promedio(self):
        self.sumar_nums()
        promedio = self.suma_total / len(self.numeros)
        return promedio

    def cuadrados_de_nums(self):
        for num in self.numeros:
            self.numeros_cuadrados.append(num**2)
        return self.numeros_cuadrados