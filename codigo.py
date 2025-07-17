def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División entre cero"
    return a / b

def calculadora():
    print("Calculadora básica en Python")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    
    operacion = input("Escribe la operación que deseas realizar: ").strip().lower()
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Entrada inválida. Debes ingresar números.")
        return

    if operacion == "suma":
        resultado = suma(a, b)
    elif operacion == "resta":
        resultado = resta(a, b)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(a, b)
    elif operacion == "division":
        resultado = division(a, b)
    else:
        print("Operación no válida.")
        return

    print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()
