Algoritmo Promedio_Notas
	Definir nota1, nota2, nota3 Como Real
	Definir promedio Como Real
	
	Escribir "Ingresa la primera nota: "
	Leer nota1
	Escribir "Ingresa la segunda nota: "
	Leer nota2
	Escribir "Ingresa la tercer nota: "
	Leer nota3
	
	promedio = (nota1 + nota2 + nota3) / 3
	
	Si promedio >= 7 Entonces
		Escribir "Promocionado"
	SiNo
		Si promedio >= 4 y promedio <7 Entonces
			Escribir "Regular"
		SiNo
			Escribir "Reprobado"
		FinSi
	FinSi
	
FinAlgoritmo
