print('--'*20)
print('soma e potencia dos valores digitados')
print('--'*20)

def soma(a,b):
    return a+b

def pot(n):
    return n**2

a = int(input('digite um valor: '))
b = int(input('digite outro valor: '))

resultado = soma(a,b)
potencia = pot(resultado)
print(f'{a} + {b} = {resultado}')
print(f'{resultado}^2 = {potencia}')