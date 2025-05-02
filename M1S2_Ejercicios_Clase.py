# Ejercicio No. 1
"""Escribe un programa que genere una lista de los 20 primeros números pares usando for y
15 primeros números impares usando while."""

# lista_numeros_pares = []
# lista_numeros_impares = []
# for numeros in range(1, 41):
#     if numeros % 2 == 0:
#         lista_numeros_pares.append(numeros)
#     else:
#         while len(lista_numeros_impares) < 15:
#             lista_numeros_impares.append(numeros)
#             break
#
# print(f"Los 20 primeros números pares son: {lista_numeros_pares}")
# print(f"Los 15 primeros números impares son: {lista_numeros_impares}")

# Ejercicio No. 2
"""Pide al usuario un número n y calcula la suma de los primeros n números naturales usando for y luego con while."""

# n:int = int(input("Ingresa un número entero positivo: "))
# suma_for:int = 0
# suma_while:int = 0
# contador:int = 0
#
# for numero in range(1, n + 1):
#     suma_for += numero
#
# while contador < n:
#     contador += 1
#     suma_while += contador
#
# print(f"La suma de los primeros {n} números naturales usando for es: {suma_for}")
# print(f"La suma de los primeros {n} números naturales usando while es: {suma_while}")

# Ejercicio No. 3
"""Escribe un programa que calcule el factorial de un número dado usando ambos bucles"""

# n:int = int(input("Ingresa un número entero positivo: "))
# factorial_for:int = 1
# factorial_while:int = 1
# contador:int = 0
#
# for numero in range(1, n + 1):
#     factorial_for *= numero
#
# while contador < n:
#     contador += 1
#     factorial_while *= contador
#
# print(f"El factorial de {n} usando for es: {factorial_for}")
# print(f"El factorial de {n} usando while es: {factorial_while}")