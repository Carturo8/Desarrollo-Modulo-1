nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio:float = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 < 7:
    print("Regular")
else:
    print("Reprobado")