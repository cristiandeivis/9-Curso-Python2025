"""Exercício 64:
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
c=0
soma = 0
qtd = 0
while c != 999:
    numero = int(input('Digite um número ou 999 para sair: '))
    if numero != 999:
        soma += numero
        qtd += 1
    c=numero
print(f'A soma é {soma} e foram digitados {qtd} números')


