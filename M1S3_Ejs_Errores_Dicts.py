"""El siguiente código intenta sumar los precios de un diccionario, pero no funciona.
Encuentra el error y corrígelo para que calcule correctamente el total. Python"""

precios = {"manzana": 1.5, "banana": 0.8, "pera": 1.2}
total = 0
for precio in precios.values():
    total += precio
print(total)

# -----
usuario = {"nombre": "Ana", "edad": 30}
print(usuario["nombre"], usuario["edad"])

# ----
dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
fusion = dic1 | dic2
print(fusion)

# ----
inventario = {"laptop": 5, "mouse": 10}
inventario.update({"laptop": 3})
print(inventario)

"""El siguiente código debería contar cuántas veces aparece cada palabra en una lista, pero no funciona correctamente. 
¿Puedes encontrar el error y arreglarlo?"""

palabras = ["manzana", "banana", "manzana", "pera", "banana", "manzana"]
contador = {}
for word in palabras:
    if word in contador:
        contador[word] += 1
    else:
        contador[word] = 1
print(contador)