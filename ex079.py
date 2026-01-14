"""DESAFIO 079
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        opt = (input('Deseja continuar? S/N '))
        if opt in 'Nn':
            break
    else:
        print('Este número já existe!')
num.sort()
print(num)      