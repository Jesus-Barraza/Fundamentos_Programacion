#Programa de operaciones matemáticas

#Crear un programa que realice una operacion matematica suma o resta o multiplicacion o division
'''
  a) Incluir funciones
  b) Incluir manejo de excepciones
'''

#Importaciones
import os
import math

#Definiciones
operacion=0
def su(n1,n2):
    sum=n1+n2
    return sum
def re(n1,n2):
    res=n1-n2
    return res
def mu(n1,n2):
    mul=n1*n2
    return mul
def di(n1,n2):
    try:
        div=n1/n2
    except ZeroDivisionError:
        div="No se puede dividir entre zero"
    return div
def po(n1,n2):
    pot=n1**n2
    return pot
def ra(n1,n2):
    rai=n1**(1/n2)
    return rai

while opera!=7:
    try:
        os.system("clear")
        print("\n\t\t..:: CALCULADORA BÁSICA :::. \n\t 1.- Suma \n\t 2.- Resta \n\t 3.- Multiplicacion \n\t 4.- Division \n\t 5.- Potencia \n\t 6.- Raiz \n\t 7.-Salir")
        opera=int(input("\n\t\t Selecciona un opción:  "))

        if opera>=1 and opera<=6:
                #entrada
            os.system("clear")
            print("\n\t Ingrese los numeros: ")
            num1=float(input("Número #1: "))
            num2=float(input("Número #2: "))

            ope=""
            if opera==1:
                ope=f"{num1} + {num2} = {round(su(num1,num2),3)}"
            elif opera==2:
                ope=f"{num1} - {num2} = {round(re(num1,num2),3)}"
            elif opera==3:
                ope=f"{num1} * {num2} = {round(mu(num1,num2),3)}"       
            elif opera==4:
                try:
                    ope=f"{num1} / {num2} = {round(di(num1,num2),3)}"
                except TypeError:
                    ope=f"{di(num1,num2)}"
            elif opera==5:
                ope=f"{num1} ^ {num2} = {round(po(num1,num2),3)}"
            elif opera==6:
                try:
                    ope=f"raiz {num2} de {num1} = {round(ra(num1,num2),3)}"
                except TypeError:
                    ope=f"Este número entra en el rango de los imaginarios"
            else:
                print("Este operacion no existe")

            print(f"\n\t\t {ope}")
            input("\n...Oprima enter para continuar ...")

        elif operacion==7:
            os.system("clear")
            print("\n\t\t..::Terminó la ejecución del SW::..")

        else:
            print("\n\tOperación no válida, vuelva a intentarlo otra vez")
            input("\n...Oprima enter para continuar ...")
    except ValueError:
        print("\n\tIngrese solo valores numéricos")
        input("\n...Oprima enter para continuar ...")
    except:
        print("\n\tOperación no válida, vuelva a intentarlo otra vez")
        input("\n...Oprima enter para continuar ...") 
