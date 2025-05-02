# 1. Números mayores o iguales a 1000.
"""Escribir un programa que lea n números enteros y determine cuántos de ellos son mayores o iguales a 1000."""

# numeros:str = input("Ingrese una lista de números enteros separada por comas: ")
# numeros:str = numeros.split(",")
# lista_numeros:list[int] = [int(x) for x in numeros]
# lista_numeros_mayores:list[int] = []
# contador:int = 0
# for numero in lista_numeros:
#     if numero >= 1000:
#         lista_numeros_mayores.append(numero)
#         contador += 1
# print(f"Los números mayores o iguales a 1000 son: {contador} --> {lista_numeros_mayores}")

# 2. Cálculo de áreas de triángulos
"""Confeccionar un programa que lea n pares de datos (base y altura) correspondientes a triángulos. Debe mostrar:
    Base, altura y superficie de cada triángulo.
    Cantidad de triángulos con superficie mayor a 12."""

# base_altura:str = input("Ingrese los pares de datos (base,altura) separados por comas: ")  # ejemplo: 30,40,20.5,30.5,20.5
# lista_base_altura:list = base_altura.split(",")
# lista_base_altura = [round(float(x.strip()), 2) for x in lista_base_altura]  # convertimos a float
# contador_superficie_mayor_12:float = 0
#
# # Creamos los pares
# datos_triangulo = []
# for i in range(0, len(lista_base_altura), 2):  # saltamos de 2 en 2
#     if i + 1 < len(lista_base_altura):  # verificamos que exista el segundo elemento del par
#         superficie = round((lista_base_altura[i] * lista_base_altura[i + 1]) / 2, 2)
#         base_altura_superficie = [lista_base_altura[i], lista_base_altura[i + 1], superficie]
#         datos_triangulo.append(base_altura_superficie)
#         if superficie > 12:
#             contador_superficie_mayor_12 += 1
#
# print(f"Pares de datos: {datos_triangulo}")
# print(f"Cantidad de triángulos con superficie mayor a 12: {contador_superficie_mayor_12}")