def calculadora(operacion, numero1, numero2):
    if operacion == 1:
        print('El resultado es: ' + str(numero1 + numero2))
    elif operacion == 2:
        print('El resultado es: ' + str(numero1 - numero2))
    elif operacion == 3:
        print('El resultado es: ' + str(numero1 * numero2))
    elif operacion == 4:
        print('El resultado es: ' + str(numero1 / numero2))



print ("Bienvenido a la calculadora \n estas son las operaciones que puedes hacer: \n 1 - Suma \n 2- Resta \n 3 - Multiplicacion \n 4 - Division ")
try:
    operacion = int(input("Introduce el numero de operacion que quieres realizar: "))
    numero1 = int(input("Introduce el primer numero: "))
    numero2 = int(input("Introduce el segundo numero: "))
except ValueError:
    print("Por favor introduce solo numero")
else:
    resultado = calculadora(operacion, numero1, numero2)
    print(resultado)
    print('gracias')