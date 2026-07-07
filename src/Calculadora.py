def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: No se puede dividir entre cero"

def modulo(n1, n2):
    return n1 % n2

def inv(n1):
    if n1 != 0:
        return 1 / n1
    else:
        return "Error: No existe inverso de cero"


if __name__ == "__main__":
    num1 = float(input("Ingresa un número: "))
    num2 = float(input("Ingresa otro número: "))

    operador = input("Ingresa el operador (+, -, *, /, %): ")

    if operador == "+":
        print("Resultado:", suma(num1, num2))

    elif operador == "-":
        print("Resultado:", resta(num1, num2))

    elif operador == "*":
        print("Resultado:", mult(num1, num2))

    elif operador == "/":
        print("Resultado:", div(num1, num2))

    elif operador == "%":
        print("Resultado:", modulo(num1, num2))

    else:
        print("Operador no válido")l