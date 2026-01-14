"""DESAFIO 082

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    opt = input('Deseja continuar? ')
    if opt in "Nn":
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print (f'A lista é {lista}')
print (f'Os números pares são: {pares}')
print (f'Os números ímpares são: {impares}')
