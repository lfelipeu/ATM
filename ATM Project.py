#Este programa simule un cajero automatica que lea un monto y entrega la cantidad minima de billetes

import time  #Imprime la libreria time con la fecha y hora del sistema

n = int(input("Ingrese cuantas veces quiere repetir el proceso: "))

while n > 0:  # Habilita el ciclo While

    valor = int(input("Ingrese el monto de dinero a calcular: "))  #Imprime el monto del dinero escogido por el usuario
    
    if valor // 50000 >= 1:  # Imprime la condición del billete de 50 mil
        billetes_de_50 = valor // 50000  #Operacion matematica para el billete de 50 mil
        valor = valor % 50000
        print(f"Billetes de 50 mil: {billetes_de_50}") # Imprime los billetes de 50 mil
        time.sleep(2)  # Para que se espere 2 segundo y despues imprima el siguiente billete

    if valor // 20000 >= 1:  # Imprime la condición del billete de 20 mil
        billetes_de_20 = valor // 20000 #Operacion matematica para el billete de 20 mil
        valor = valor % 20000
        print(f"Billetes de 20 mil: {billetes_de_20}") # Imprime los billetes de 20 mil
        time.sleep(2)  # Para que se espere 2 segundo y despues imprima el siguiente billete

    if valor // 10000 >= 1:  # Imprime la condición del billete de 10 mil
        billetes_de_10 = valor // 10000 #Operacion matematica para el billete de 10 mil
        valor = valor % 10000
        print(f"Billetes de 10 mil: {billetes_de_10}")  # Imprime los billetes de 10 mil
        time.sleep(2)  # Para que se espere 2 segundo y despues imprima el siguiente billete

    if valor // 5000 >= 1:  # Imprime la condición del billete de 5 mil
        billetes_de_5 = valor // 5000 #Operacion matematica para el billete de 5 mil
        valor = valor % 5000
        print(f"Billetes de 5 mil: {billetes_de_5}")  # Imprime los billetes de 5 mil
        time.sleep(2)  # Para que se espere 2 segundo y despues imprima el siguiente billete

    if valor // 2000 >= 1:  # Imprime la condición del billete de 2 mil
        billetes_de_2 = valor // 2000  #Operacion matematica para el billete de 2 mil
        valor = valor % 2000
        print(f"Billetes de 2 mil: {billetes_de_2}")  # Imprime los billetes de 2 mil
        time.sleep(2)  # Para que se espere 2 segundo y despues imprima el siguiente billete

    if valor // 1000 >= 1:  # Imprime la condición del billete de mil
        billetes_de_1 = valor // 1000  #Operacion matematica para el billete de mil
        valor = valor % 1000
        print(f"Billetes de mil: {billetes_de_1}")  # Imprime los billetes de mil
        time.sleep(2)  # Para que se espere 2 segundo y despues imprima el siguiente billete

    if valor > 0:  #Imprime la condicion que si el numero ingresado es menor que la cantidad de billetes dice que es incorrecto
        print(f"El monto ingresado es menor que la cantidad de los billetes.")
        time.sleep(3)
    n -= 1
