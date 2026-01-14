"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.
"""

nome = ['','','','']
idade = [0,0,0,0]
sexo =['','','','']
media = 0
maior = 0
quantidade = 0
for c in range (0,4):
    nome[c] = input('Digite o seu nome: ')
    idade[c] = int(input('Digite a sua idade: '))
    sexo[c]= input('Digite o seu sexo M ou F: ').lower()
    media = media+idade[c]
    if sexo[c] == 'm' and c == 0:
        maior = idade[c]
        nome_maior = nome[c]
    if idade[c] > maior and sexo[c] == 'm':
        maior = idade[c]
        nome_maior = nome[c]
    if sexo[c] == 'f' and idade[c] < 20:
        quantidade += quantidade+1
media = media/4
print (f'A média de idade é {media}')
print (f'O homem mais velho é {nome_maior.capitalize()} e sua idade é {maior}')
print (f'Existem {quantidade} de mulheres com menos de 20 anos.')