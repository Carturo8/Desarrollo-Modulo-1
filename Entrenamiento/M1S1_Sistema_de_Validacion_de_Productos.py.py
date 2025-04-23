import re

### Bucle para solicitar y validar el nombre del producto
# Se utiliza un bucle while para seguir pidiendo el nombre hasta que sea válido
while True:
    producto = input("Ingresa el nombre del producto: ").strip() # Pedir nombre y eliminar espacios en blanco
    if len(producto) > 25: # Validar longitud del nombre
        print("El nombre del producto no debe exceder los 25 caracteres.") # Mensaje de error
    elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", producto): # Validar caracteres permitidos
        print("Entrada inválida. Ingresa un nombre válido.") # Mensaje de error
    else:
        producto = producto.title() # Convertir a formato título
        break # Salir del bucle si el nombre es válido

### Bucle para solicitar y validar el precio unitario del producto
# Se utiliza un bucle while para seguir pidiendo el precio hasta que sea válido
while True:
    try:
        precio = round(float(input("Ingresa el precio unitario del producto: ")), 2) # Pedir precio y redondear a 2 decimales
        if precio > 0: # Validar que el precio sea positivo
            break  # Salir del bucle si el precio es positivo
        else:
            print("El precio debe ser un número positivo.") # Mensaje de error
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.") # Mensaje de error

### Bucle para solicitar y validar la cantidad del producto
# Se utiliza un bucle while para seguir pidiendo la cantidad hasta que sea válida
while True:
    try:
        cantidad = int(input("Ingresa la cantidad del producto: ")) # Pedir cantidad y convertir a entero
        if cantidad > 0: # Validar que la cantidad sea positiva
            break # Salir del bucle si la cantidad es positiva
        else:
            print("La cantidad debe ser un número entero positivo.") # Mensaje de error
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.") # Mensaje de error

### Bucle para solicitar y validar el porcentaje de descuento
# Se utiliza un bucle while para seguir pidiendo el descuento hasta que sea válido
while True:
    try:
        descuento = round(float(input("Ingresa el porcentaje de descuento: ")), 2) # Pedir descuento y redondear a 2 decimales
        if descuento >= 0 and descuento <= 100: # Validar que el descuento esté entre 0 y 100
            break # Salir del bucle si el descuento es válido
        else:
            print("El descuento debe ser un número entre 0 y 100.") # Mensaje de error
    except ValueError:
        print("Entrada inválida. Ingresa un número válido.") # Mensaje de error

# Calcular el total sin descuento
total = round(precio * cantidad, 2) # Redondear el total a 2 decimales

# Calcular el total con descuento
valor_descuento = round(total * descuento/100, 2) # Calcular el valor del descuento
total_dc = round(total - valor_descuento, 2) # Redondear el total con descuento a 2 decimales

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
