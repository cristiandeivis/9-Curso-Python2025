"""
Faça um programa que leia um número inteiro e 
diga se ele é ou não um número primo.
"""
num = int(input('Digite um número inteiro: '))
count = 0
for c in range (1,num+1):
    div = num%c
    if div == 0:
        count = count+1
if count == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')
