def ingresar_numeros():
    numeros = []
    while True:
        try:
            numero = float(input("Ingrese un número (o cualquier otra tecla para finalizar): "))
            numeros.append(numero)
        except ValueError:
            break
    return numeros

def separar_numeros(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

def obtener_mayor(lista):
    if lista:
        return max(lista)
    else:
        return None

numeros = ingresar_numeros()
pares, impares = separar_numeros(numeros)

if pares:
    mayor_par = obtener_mayor(pares)
    print(f"El mayor número par ingresado es: {mayor_par}")
else:
    print("No se ingresaron números pares.")

if impares:
    mayor_impar = obtener_mayor(impares)
    print(f"El mayor número impar ingresado es: {mayor_impar}")
else:
    print("No se ingresaron números impares.")

mayor_total = obtener_mayor(numeros)
if mayor_total is not None:
    print(f"El mayor número ingresado en total es: {mayor_total}")
else:
    print("No se ingresaron números.")
