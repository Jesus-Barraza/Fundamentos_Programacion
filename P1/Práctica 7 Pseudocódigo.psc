Algoritmo factura
	
	//definiciones
	Definir factur,factur_impuest,impuest Como Real;
	impuest=18;
	
	//Lecturas
	Escribir "Inserte el precio de la factura";
	Leer factur;

	//Cálculos
	factur_impuest=factur+(factur*(impuest/100));

	//Impresiones
	Imprimir "El precio de la factura incluyendo el impuesto es de: $",factur_impuest;

FinAlgoritmo
