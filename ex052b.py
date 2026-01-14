"""
Faça um programa que leia um número inteiro e 
diga se ele é ou não um número primo.
"""
soma = 0
numero = int(input('Digite um número inteiro: '))
for c in range (1,numero+1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        soma +=1
    else:
        print('\033[31m', end=' ')
    print (c, end=' ')
    print('\33[m', end =' ')
print(f'\nO número {numero} foi divisível {soma} vezes!')
if soma == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')
    