inicio = "si"
while inicio == "si":
    print("Bienvenido a la calculadora")
    print("Estas son las operaciones que puedes realizar")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicación")
    print("4 - División")
    print(" ")
    try:
        a = int(input("Cuál es el número de operación que deseas realizar? : "))
        x = int(input("Introduce el primer número : "))
        y = int(input("Introduce el segundo número : "))

    except ValueError:
        print("El caractér ingresado no es un número")
    else:
        if a == 1:
            resultado = x + y
        elif a == 2:
            resultado = x - y
        elif a == 3:
            resultado = x * y
        elif a == 4:
            resultado = x / y

        print("La solución es : " + str(resultado))

    inicio = input("Quieres continuar? si/no : ")
    print(" ")