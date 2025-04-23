"1. Pide al usuario su nombre y edad, y muestra un mensaje que diga:" "Hola [nombre], tienes [edad] años."

def Nombre_Edad ():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    print(f"Hola {nombre}, tienes {edad} años.")

#Nombre_Edad()

"2. Pide dos números enteros y muestra la suma de ambos."

def Suma_Dos_Numeros_Enteros():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")

#Suma_Dos_Numeros_Enteros()

"3. Pide dos números decimales (float) y muestra su multiplicación."

def Multiplicacion_Dos_Numeros_Decimales():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    multiplicacion = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    
#Multiplicacion_Dos_Numeros_Decimales()

"4. Pide un número entero y muestra el doble y el triple de ese número, separados por coma."

def Doble_Triple_Numero_Entero():
    num = int(input("Ingresa un número entero: "))
    doble = num * 2
    triple = num * 3
    print(f"El doble y el triple de {num} es: {doble}, {triple}, respectivamente.")
    
#Doble_Triple_Numero_Entero()

"5. Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces."

def Repetir_Palabra():
    palabra = input("Ingresa una palabra: ")
    num = int(input("Ingresa un número entero: "))
    repeticion = palabra * num
    print(f"La palabra '{palabra}' repetida {num} veces es: {repeticion}")