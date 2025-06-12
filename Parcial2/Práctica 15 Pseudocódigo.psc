Algoritmo otra_tienda_mas
	
	//Definiciones pt.1
	Definir cont,cantidad,cont_final Como Entero;
	Definir precio,desc_por,desc,iva_por,iva,total,total_acu Como Real;
	total_acu=0
	cont_final=0
	
	//Lecturas pt.1
	Escribir "                 Otra tienda genérica SA de CV";
	Escribir "A partir de este punto en adelante se hará el proceso de introducir productos bajo cantidad y precio";
	Escribir "El número que inserte será el número de productos únicos a introducir";
	Escribir "Una vez ponga ese número de productos únicos se realizará el bucle hasta terminar el n° de veces";
	Escribir "Ingrese el n° de veces que se realizará el bucle";
	Leer cont_final;
	
	Para cont=1 hasta cont_final Con Paso 1 Hacer
		//Definiciones pt.2
		cantidad=0
		precio=0
		
		//Lecturas pt.2
		Escribir "Número de repetición hasta ",cont_final,": ",cont;
		Escribir "Ingrese el n° de productos";
		Leer cantidad;
		Escribir "Ingrese el precio unitario del producto ($)";
		Leer precio
		
		//Cálculos
		iva_por=16;
		
		Si cantidad>5 Entonces
			desc_por=10;
		SiNo
			desc_por=5;
		FinSi
		
		desc=desc_por*precio/100;
		iva=(precio-desc_por)*iva/100;
		total=precio-desc+iva;
		total_acu=total_acu+total;
	FinPara
	
	//Impresiones
	Imprimir "Finalizado!";
	Imprimir "Precio acumulado total: $",total_acu;
	Imprimir "N° de veces que se repitió: ",cont_final
FinAlgoritmo
