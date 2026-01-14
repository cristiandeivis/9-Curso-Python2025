#DESAFIO 078
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for c in range(0,5):
    numeros.append(int(input('Digite um número: ')))
print (f'A lista digitada é {numeros}')
maior = 0
menor = 0
posicao_maior =''
posicao_menor =''
for c,v in enumerate(numeros):
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print (f'O maior número é: {maior} nas posições:',end = ' ')
for c,v in enumerate(numeros):
    if v == maior:
        print(f' {c}...', end ='')
print (f'\nO menor número é: {menor} nas posições:',end = ' ')
for c,v in enumerate(numeros):
    if v == menor:
        print(f'{c}...', end =' ')