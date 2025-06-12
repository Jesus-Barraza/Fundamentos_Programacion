Algoritmo descuentos
	
	//definiciones
	Definir precio,descuento,adescuentar,precio_descuentado como entero;
	
	//Lecturas
	Escribir "Ingresa el precio del producto ($)";
	Leer precio;
	Escribir "Ingresa el descuento a descuentar (%)";
	Leer descuento;
	
	//Cálculos
	adescuentar=(descuento/100)*precio;
	precio_descuentado=precio-adescuentar;

	//Impresiones
	Imprimir "El precio final tras el descuento es de: $",precio_descuentado;

FinAlgoritmo
