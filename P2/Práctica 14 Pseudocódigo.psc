Algoritmo 	paga_infinita
	
	//Definiciones
	Definir precio,iva,por_iva,desc,desc_por,total,total_acu Como Real;
	Definir cantidad,repeti Como Entero;
	Definir repeticion Como Cadena;
	
	//Escrituras
	Escribir "Tienda de la esquina que no importa su nombre SA de CV";
	
	//Ciclo entero
	repeticion="Si";
	Mientras repeticion="Si"o repeticion="si" o repeticion="SI" o repeticion="sI" Hacer
		//Lecturas
		Escribir "Ingrese la cantidad del producto a comprar";
		Leer cantidad;
		Escribir "Ingrese el precio inicial del producto a comprar ($)";
		Leer precio;
		
		//Cálculos
		iva_por=16;
		desc_por=0;
		total_acu=0;
		
		Si cantidad>5 Entonces
			desc_por=10;
		SiNo
			desc_por=5;
		FinSi
		
		desc=precio*desc_por/100;
		iva=(precio-desc)*iva_por/100;
		total=precio-desc+iva;
		total_acu=total_acu+total;
		repeti=repeti+1;
		
		//Impresiones pt.1
		Imprimir "¿Deseas capturar otro producto? (Si/No)";
		Leer repeticion;	
	FinMientras
	
	//Impresiones pt.2
	Imprimir "Precio total a pagar: $",total_acu
	Imprimir "N° de productos únicos colocados: ",repeti
	
FinAlgoritmo
