"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
já são maiores.
"""
from datetime import date
maior = 0
menor = 0
ano = date.today().year
print (ano)
for c in range (7):
    idade = int(input('Digite o ano de Nascimento: '))
    if (ano-idade) >= 18:
        maior+=1
    else:
        menor+=1
print (f'{maior} pessoas são maiores de idade')
print (f'{menor} pessoas são menores de idade')
