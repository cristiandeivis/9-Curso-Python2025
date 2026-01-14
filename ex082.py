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
    opt = str(input('Deseja continuar S/N?: '))
    if opt in ('Nn'):
        break
for c in range (len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print (lista)
print (pares)
print (impares)