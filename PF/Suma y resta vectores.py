'''Porción del código mayor - Suma y resta de vectores'''

#Importaciones
import os
import math

#Definiciones pt.1
Radianes=1
Sexagesimales=(math.pi/180)
Gradianes=(360/400)*(math.pi/180)
Newthon=1
Libras=4.45
n=0
decision1="0"
decision2="0"  
potencia1="0"
potencia2="0"
medida1="0"
medida2="0"
angulo1="0"
angulo2="0"
opera="0"
accion1="0"
accion2="0"
ciclo="2"

def convera(ang,conv1):
    converta=ang*conv1
    return converta
def converl(lad,conv2):
    convertl=lad*conv2
    return convertl
def Lado_x(convertl,converta):
    grad=convertl*math.cos(converta)
    return grad
def Lado_y(convertl,converta):
    grad2=convertl*math.sin(converta)
    return grad2
def Lado_T(grad1,grad2):
    gradt=(grad1**2+grad2**2)**(1/2)
    return gradt
def angulo(grad1,grad2):
    try:    
        angt=math.atan(grad2/grad1)
    except ZeroDivisionError:
        angt=(math.pi/2)
    finally:
        if grad1<0:
            if grad2>=0:
                angt=angt+math.pi
            elif grad2<0:
                angt=angt-math.pi
    return angt


while ciclo!="3":
    #Lecturas pt.1 General
    os.system("cls")
    os.system("clear")
    print("\n\t\t -/|Cálculo de suma y resta de vectores|\-")
    while opera!="1" and opera!="2" and opera!="+" and opera!="-":
        opera=input("\n\t Selecciona la operación a realizar \n (1)Suma (+) \n (2)Resta (-) \n(1/2): ")
        if opera!="1" and opera!="2":
            print("Selección no válida")

    if ciclo=="2":
        #Lecturas pt.2 Vector 1
        os.system("cls")
        os.system("clear")
        while decision1!="1" and decision1!="2" and decision1!="n" and decision1!="lb":
            decision1=input("\n\t Seleccione la medición de fuerza del primer vector: \n (1)Newtons (N) \n (2)Libras de fuerza (lb) \n(1/2): ").lower()
            if decision1!="1" and decision1!="2" and decision1!="n" and decision1!="lb":
                print("\n\t\tSelección no válida")
        while type(potencia1) is not float:
            try:
                potencia1=float(input("\n Ingrese la cantidad de fuerza en el primer vector en números: "))
            except ValueError:
                print("Selección no válida")
        while medida1!="1" and medida1!="2" and medida1!="3" and medida1!="°" and medida1!="rad" and medida1!="g":
            medida1=input("\n\t Seleccione la medición de ángulo del primer vector: \n (1)Grados sexagesimales (°) \n (2)Radianes (rad) \n (3)Gradianes (g) \n(1/2/3): ").lower()
            if medida1!="1" and medida1!="2" and medida1!="3" and medida1!="°" and medida1!="rad" and medida1!="g":
                print("\n\t\tSelección no válida")
        while type(angulo1) is not float:
            try:
                angulo1=float(input("\n Ingrese la inclinación del primer vector en números (donde 0 es la coordenada x positiva): "))
            except ValueError:
                print("Selección no válida")
        n=n+1
        

    #Lecturas pt.3 Vector 2
    os.system("cls")
    os.system("clear")
    while decision2!="1" and decision2!="2" and decision2!="n" and decision2!="lb":
        decision2=input("\n\t Seleccione la medición de fuerza del segundo vector: \n (1)Newtons (N) \n (2)Libras de fuerza (lb) \n(1/2): ").lower()
        if decision2!="1" and decision2!="2" and decision2!="n" and decision2!="lb":
            print("\n\t\tSelección no válida")
    while type(potencia2) is not float:
        try:
            potencia2=float(input("\n Ingrese la cantidad de fuerza en el segundo vector en números: "))
        except ValueError:
            print("Selección no válida")
    while medida2!="1" and medida2!="2" and medida2!="3" and medida2!="°" and medida2!="rad" and medida2!="g":
        medida2=input("\n\t Seleccione la medición de ángulo del segundo vector: \n (1)Grados sexagesimales (°) \n (2)Radianes (rad) \n (3)Gradianes (g) \n(1/2/3): ").lower()
        if medida2!="1" and medida2!="2" and medida2!="3" and medida2!="°" and medida2!="rad" and medida2!="g":
            print("\n\t\tSelección no válida")
    while type(angulo2) is not float:
        try:
            angulo2=float(input("\nIngrese la inclinación del primer vector en números (donde 0 es la coordenada x positiva): "))
        except ValueError:
            print("Selección no válida")
    n=n+1

    #Cálculos pt.1
    if decision1=="1" or decision1=="n":
        tipo1=Newthon
    elif decision1=="2" or decision1=="lb":
        tipo1=Libras
    if decision2=="1" or decision2=="n":
        tipo2=Newthon
    elif decision2=="2" or decision2=="lb":
        tipo2=Libras
    if medida1=="1" or medida1=="°":
        tipoa1=Sexagesimales
    elif medida1=="2" or medida1=="rad":
        tipoa1=Radianes
    elif medida1=="3" or medida1=="g":
        tipoa1=Gradianes
    if medida2=="1" or medida2=="°":
        tipoa2=Sexagesimales
    elif medida2=="2" or medida2=="rad":
        tipoa2=Radianes
    elif medida2=="3" or medida2=="g":
        tipoa2=Gradianes
    if opera=="2" or opera=="-":
        tmedida2=tmedida2*(-1)
        texto1="resta"
    elif opera=="1" or opera=="+":
        texto1="suma"

    #Cálculos pt.2
    tmedida1=float(converl(potencia1,tipo1))
    tangulo1=float(convera(angulo1,tipoa1))
    tmedida2=float(converl(potencia2,tipo2))
    tangulo2=float(convera(angulo2,tipoa2))
    xme1=Lado_x(tmedida1,tangulo1)
    xme2=Lado_x(tmedida2,tangulo2)
    yme1=Lado_y(tmedida1,tangulo1)
    yme2=Lado_y(tmedida2,tangulo2)
    xmet=xme1+xme2
    ymet=yme1+yme2
    totall=Lado_T(xmet,ymet)
    totala=angulo(xmet,ymet)

    #Lecturas pt.4 Decisión de impresión
    os.system("cls")
    os.system("clear")
    while accion1!="1" and accion1!="2" and accion1!="n" and accion1!="lb":
        accion1=input("\n\t¿Con qué medida de fuerza desea ver el resultado? \n (1)Newtons (N)\n (2)Libras de fuerza (lb) \n(1/2): ").lower()
        if accion1!="1" and accion1!="2" and accion1!="n" and accion1!="lb":
            print("\n\t Selección incorrecta")
    while accion2!="1" and accion2!="2" and accion2!="3" and accion2!="°" and accion2!="rad" and accion2!="g":
        accion2=input("\n\t¿Con qué medida de ángulo desea ver el resultado? \n (1)Grados sexagesimales (°)\n (2)Radianes (rad)\n (3)Gradianes (g) \n(1/2/3): ").lower()
        if accion2!="1" and accion2!="2" and accion2!="3" and accion2!="°" and accion2!="rad" and accion2!="g":
            print("\n\t Selección no válida")

    #Cálculos pt.3
    if accion1=="1" or accion1=="n":
        convertl=Newthon
        texto2="N"
    elif accion1=="2" or accion1=="lb":
        convertl=Libras
        texto2="lb"
    if accion2=="1" or accion2=="°":
        converta=Sexagesimales
        texto3="°"
    elif accion2=="2" or accion2=="rad":
        converta=Radianes
        texto3="rad"
    elif accion2=="3" or accion2=="g":
        converta=Gradianes
        texto3="g"

    #Cálculos pt.4
    total_lado=converl(totall,(1/convertl))
    total_angulo=convera(totala,(1/converta))

    #Impresiones
    os.system("cls")
    os.system("clear")
    print("\n\t\tSe ha finalizado el cálculo")
    print(f"\n\t El resultado de la {texto1} de los vectores da como resultado un vector con una potencia de \033[1m{round(total_lado,5)}{texto2}\033[0m y un ángulo de \033[1m{round(total_angulo,5)}{texto3}\033[0m")
    print(f"Se han registrado un total de {n} vectores")
    print("\nPresione 'enter' para continuar")

    input()

    #Ciclo pt.1
    ciclo="0"
    while ciclo!="1" and ciclo!="2" and ciclo!="3":
        ciclo=input("\n\t Seleccione una acción a continuación \n (1)Sumar/restar otro vector al resultado\n (2)Sumar/restar otros 2 vectores\n (3)Salir \n(1/2/3): ")
        if ciclo!="1" and ciclo!="2" and ciclo!="3":
            print("Selección no válida")

    #Definiciones pt.2
    medida1=totall
    angulo1=totala
    decision1=accion1
    medida1=accion2
    decision2="0"  
    potencia2="0"
    medida2="0"
    angulo2="0"
    opera="0"
    accion1="0"
    accion2="0"
    tmedida2=0
    tangulo2=0
    xme2=0
    yme2=0

    if ciclo=="2":
        #Definiciones pt.3
        decision1="0"
        potencia1="0"
        medida1="0"
        angulo1="0"
        tmedida1=0
        tangulo1=0
        xme1=0
        yme1=0
        total_lado=0
        total_angulo=0
        totall=0
        totala=0
        n=0

os.system("cls")
os.system("clear")
print("¡Se ha finalizado el programa!")