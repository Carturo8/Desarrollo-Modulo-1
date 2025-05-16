suma: float = 0.0
promedio: float = 0.0

for i in range(0, 10, 1):
    i = float(input("Ingresa un número: "))
    suma = i + suma

promedio = suma / 10
    
print("La suma es:", suma)
print("El promedio es:", promedio)