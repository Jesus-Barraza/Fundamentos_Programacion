Algoritmo Nota_de_venta
	
	//Definiciones
	Definir codigo,cantidad Como Entero;
	Definir descripcion Como Cadena;
	Definir descuento,iva,unitario,neto,total,preciodescuento,precioiva Como Real;
	unitario=0
	cantidad=0
	iva=16
	
	//Lecturas
	Escribir "Nota de venta de productos";
	Escribir "Ingresa el c�digo del producto";
	Leer codigo;
	Escribir "Ingresa la descripci�n/el nombre del producto";
	Leer descripcion;
	Escribir "Ingresa el precio unitario del producto ($)";
	Leer unitario;
	Escribir "Ingrese el n� del producto a comprar";
	Leer cantidad;
	
	//C�lculos
	descuento=0
	Si cantidad>10 Entonces
		descuento=10
	FinSi
	
	neto=cantidad*unitario
	preciodescuento=neto*descuento/100
	precioiva=(neto-preciodescuento)*iva/100
	total=neto-preciodescuento+precioiva
	
	//Impresiones
	Imprimir "Nombre/descripci�n: ",descripcion;
	Imprimir "C�digo: ",codigo;
	Imprimir "Precio neto: $",neto;
	Imprimir "Descuento: $",preciodescuento;
	Imprimir "IVA: $",precioiva
	Imprimir "Total: $",total
	
FinAlgoritmo
