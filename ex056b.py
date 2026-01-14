"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.
"""

maior = 0
cont = 0
nome_maior = ''
total = 0
media = 0
for c in range(4):
    nome = input('Digite um nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida!')
    total = total+idade
    media = (total)/(c+1)
    if c == 0 and sexo =='M':
        maior = idade
        nome_maior = nome
    if idade > maior and sexo == 'M':
        maior = idade
        nome_maior = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print(f' O homem mais velho é {nome_maior} e sua idade e {maior}')
print(f' A média de idade e {media}')
print(f' {cont} mulheres tem menos de 20 anos')