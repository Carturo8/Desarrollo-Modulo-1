import re

# Solicitar y validar el nombre del producto
while True:
    producto = input("Ingresa el nombre del producto: ").strip()
    if len(producto) > 25:
        print("El nombre del producto no debe exceder los 25 caracteres.")
    elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", producto):
        print("Entrada inválida. Ingresa un nombre válido.")
    else:
        producto = producto.title()
        break

# Solicitar y validar el precio unitario
while True:
    try:
        precio = round(float(input("Ingresa el precio unitario del producto: ")), 2)
        if precio > 0:
            break  # Salir del bucle si el precio es positivo
        else:
            print("El precio debe ser un número positivo.")
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.")

# Solicitar y validar la cantidad del producto
while True:
    try:
        cantidad = int(input("Ingresa la cantidad del producto: "))
        if cantidad > 0:
            break # Salir del bucle si la cantidad es positiva
        else:
            print("La cantidad debe ser un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.")

# Solicitar y validar el porcentaje de descuento
while True:
    try:
        descuento = round(float(input("Ingresa el porcentaje de descuento: ")), 2)
        if descuento >= 0 and descuento <= 100:
            break # Salir del bucle si el descuento es válido
        else:
            print("El descuento debe ser un número entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.")

# Calcular el total sin descuento
total = round(precio * cantidad, 2) 

# Calcular el total con descuento
valor_descuento = round(total * descuento/100, 2)
total_dc = round(total - valor_descuento, 2)

# Mostrar la información del producto y el total con descuento
print("=====================================")
print("Información del Producto:")
print("=====================================")
print(f"Nombre del Producto: {producto}")
print(f"Precio Unitario: $ {precio}")
print(f"Cantidad: {cantidad}")
print(f"Precio Total sin Descuento: $ {total}")
print(f"Descuento: {descuento}% -- Valor: $ {valor_descuento}")
print(f"Precio Total con Descuento: $ {total_dc}")
