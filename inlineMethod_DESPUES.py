numeros = []
pares = []
impares = []

while True:
    try:
        numero = float(input("Ingrese un número (o cualquier otra tecla para finalizar): "))
        numeros.append(numero)
        pares.append(numero) if numero % 2 == 0 else impares.append(numero)
    except ValueError:
        break

if pares:
    print(f"El mayor número par ingresado es: {max(pares)}")
else:
    print("No se ingresaron números pares.")

if impares:
    print(f"El mayor número impar ingresado es: {max(impares)}")
else:
    print("No se ingresaron números impares.")

if numeros:
    print(f"El mayor número ingresado en total es: {max(numeros)}")
else:
    print("No se ingresaron números.")
