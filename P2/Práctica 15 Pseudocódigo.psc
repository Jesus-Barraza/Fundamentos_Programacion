Algoritmo otra_tienda_mas
	
	//Definiciones pt.1
	Definir cont,cantidad,cont_final Como Entero;
	Definir precio,desc_por,desc,iva_por,iva,total,total_acu Como Real;
	total_acu=0
	cont_final=0
	
	//Lecturas pt.1
	Escribir "                 Otra tienda gen�rica SA de CV";
	Escribir "A partir de este punto en adelante se har� el proceso de introducir productos bajo cantidad y precio";
	Escribir "El n�mero que inserte ser� el n�mero de productos �nicos a introducir";
	Escribir "Una vez ponga ese n�mero de productos �nicos se realizar� el bucle hasta terminar el n� de veces";
	Escribir "Ingrese el n� de veces que se realizar� el bucle";
	Leer cont_final;
	
	Para cont=1 hasta cont_final Con Paso 1 Hacer
		//Definiciones pt.2
		cantidad=0
		precio=0
		
		//Lecturas pt.2
		Escribir "N�mero de repetici�n hasta ",cont_final,": ",cont;
		Escribir "Ingrese el n� de productos";
		Leer cantidad;
		Escribir "Ingrese el precio unitario del producto ($)";
		Leer precio
		
		//C�lculos
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
	Imprimir "N� de veces que se repiti�: ",cont_final
FinAlgoritmo
