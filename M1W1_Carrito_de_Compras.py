""" 
🛒 Reto: Carrito de Compras con Condicionales

📌 Objetivo: 
Crear un programa en Python que:
    1. Permita registrar productos (nombre y precio)
    2. Calcule el total de la compra
    3. Recomiende el mejor método de pago según el monto

💳 Reglas de Recomendación
Monto               Método         Beneficio
Menos de $50.000    Efectivo       5% de descuento
$50.000 a $100.000  Tarjeta        Sin cambios
Más de $100.000     Transferencia  2% de cashback

🚫 Restricciones
✔ Permitido: if, elif, else
✖ Prohibido: Bucles, funciones, estructuras complejas

Se debe planificar el desarrollo en psint y luego codificar en python.
"""

nombre_p1 = input("Ingresa el nombre del primer producto: ")
precio_p1 = float(input("Ingresa el precio del primer producto: "))
nombre_p2 = input("Ingresa el nombre del segundo producto: ")
precio_p2 = float(input("Ingresa el precio del segundo producto: "))
nombre_p3 = input("Ingresa el nombre del tercer producto: ")
precio_p3 = float(input("Ingresa el precio del tercer producto: "))

total = round(precio_p1 + precio_p2 + precio_p3, 2)

if total < 50000:
    metodo_pago = "Efectivo"
    beneficio = "5% de descuento"
    descuento = round(total * 0.05, 2)
    total_dc = round(total * 0.95, 2)
elif 50000 <= total <= 100000:
    metodo_pago = "Tarjeta"
    beneficio = "Sin cambios"
else:
    metodo_pago = "Transferencia"
    beneficio = "2% de cashback"
    cashback = round(total * 0.02, 2)
    
print(f"""
El total de la compra es: ${total}
El método de pago recomendado es: {metodo_pago}
El beneficio otorgado es: {beneficio} ${descuento if total <= 50000 else ''} {cashback if total > 100000 else ''}
El total a pagar es: ${total_dc if total < 50000 else total}
""")