"""Desafio 084

Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoa = []
lista = []
cont = 0
while True:
    pessoa.append(str(input('Digite o nome da pessoa: ')).lower().capitalize().strip())
    pessoa.append(float(input('Digite o peso da pessoa: ')))
    cont += 1
    lista.append(pessoa[:])
    pessoa.clear()
    opt = str(input('Deseja continuar [S/N] '))
    if opt in 'Nn':
        break
maior = 0
menor = 0
for c,v in enumerate(lista):
    print (v[1])
    if c == 0:
        maior=menor=v[1]
    else:
        if v[1] > maior:
            maior = v[1]
        if v[1] < menor:
            menor = v[1]
print (f'Foram cadastradas {cont} pessoas')
print ('Os mais pesados foram: ', end = ' ')
print()
for v in lista:
    if v[1] == maior:
        print (f'{v[0]} com {v[1]} KGs', end = '')
        print()
print ('Os mais leves foram: ', end = ' ')
print()
for v in lista:
    if v[1] == menor:
        print(f'{v[0]} com {v[1]} KGs', end =' ')
        print()