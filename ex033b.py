#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

menor = n1
if n2 < menor and n2 < menor:
    menor = n2
if n3 < menor and n3 < menor:
    menor = n3
print (f'O menor número é: {menor}')
maior = n1
if n2 > maior and n2 > maior:
    maior = n2
if n3 > maior and n3 > maior:
    maior = n3
print (f' O maior número é: {maior}')