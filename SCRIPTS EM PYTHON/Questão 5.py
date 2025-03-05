def verif_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "zero"

numero = float(input("Digite um número: "))
resultado = verif_numero(numero)
print(f"O número {numero} é {resultado}.")

