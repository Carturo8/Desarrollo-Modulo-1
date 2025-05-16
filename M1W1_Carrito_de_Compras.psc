Algoritmo Carrito_de_Compras
	Definir nombre_p1, nombre_p2, nombre_p3 Como Caracter
	Definir precio_p1, precio_p2, precio_p3 Como Real
	Definir total, descuento, total_dc Como Real
	Definir metodo Como Caracter
	Definir beneficio Como Caracter
	
	Escribir "Ingresa el nombre del primer producto: "
	Leer nombre
	Escribir "Ingresa el precio del primer producto: "
	Leer precio
	Escribir "Ingresa el nombre del segundo producto: "
	Leer nombre
	Escribir "Ingresa el precio del segundo producto: "
	Leer precio
	Escribir "Ingresa el nombre del tercer producto: "
	Leer nombre
	Escribir "Ingresa el precio del tercer producto: "
	Leer precio
	
	total = precio_p1 + precio_p2 + precio_p3
	
	Si total < 50000 Entonces
		metodo_pago = "Efectivo"
		beneficio = "5% de descuento"
		descuento = total * 0.05
    	total_dc = total * 0.95
		
	SiNo
		Si total >= 50000 y total <= 100000 Entonces
			metodo_pago = "Tarjeta"
			beneficio = "Sin cambios"
		SiNo
			metodo_pago = "Transferencia"
			beneficio = "2% de cashback"
			cashback = total * 0.02
		FinSi
	FinSi
	
Escribir "El total de la compra es: ", total
Escribir "El método de pago recomendado es: ", metodo
Escribir "El beneficio otorgado es: ", beneficio
Escribir "El total a pagar es: ", total

FinAlgoritmo
