Algoritmo precios
	
	//Definiciones
	Definir cant_prod,descuento10,descuento Como Entero;
	Definir prec_prod,prec_final Como Real;
	descuento10=10;
	descuento=5;
	
	//Lecturas
	Escribir "Calculadora de precios";
	Escribir "Ingrese el número del producto a comprar";
	Leer cant_prod;
	Escribir "Ingrese el precio del producto a comprar ($)";
	Leer prec_prod;
	
	//Cálculos
	Si cant_prod>=10
		prec_final=(prec_prod*cant_prod)-(prec_prod*cant_prod*descuento10/100);
	SiNo
		prec_final=(prec_prod*cant_prod)-(prec_prod*cant_prod*descuento/100);
	FinSi
	
	//Impresiones
	Imprimir "El cálculo de precios finalizó";
	Imprimir "El precio a pagar es de: $",prec_final;
	
FinAlgoritmo
