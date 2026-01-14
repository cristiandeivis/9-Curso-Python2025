"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.
"""
maior = 0
menor = 0
for c in range (5):
    peso = float(input('Digite o seu peso: '))
    if maior == 0 or menor == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso 
print (f'O mais pesado é {maior} e mais magro é {menor}')
