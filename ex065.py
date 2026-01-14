"""Exercício 65:
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
Meu programa
"""
opt = 'S'
numero = 0
cont = 1
media = 0
numero = int(input('Digite um número: '))
maior = numero
menor = numero
soma = numero
while opt != 'N':
    opt = input('Deseja Continuar? ').strip().upper()[0]
    if opt == 'S':
        numero = int(input('Digite um número: '))
        soma += numero
        cont += 1
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma/cont
print(f'Você digitou {cont} números')
print(f'A média é {media:.2f}, o maior valor é {maior} e o menor valor é {menor}')


