def soma(num1,num2):
    resultado = num1 + num2
    if resultado % 2 != 0:
        return resultado
    else:
        return None

num1 = int(input('digite um valor: '))
num2 = int(input('digite outro valor: '))

soma_impar = soma(num1,num2)

if soma_impar is not None:
    print(f"A soma dos valores {num1} e {num2} equivale a {soma_impar}.")
else:
    print('O resultado da soma é um valor par, não sendo possível a realização da soma.')
