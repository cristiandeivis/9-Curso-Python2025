"""Desafio 085

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""

lista = [[],[]]
numero = 0
for c in range (1,8):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print (f'Pares {lista[0]}', end = ' ')
print (f'\nImpares {lista[1]}', end = ' ')