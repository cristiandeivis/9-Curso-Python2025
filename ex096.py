"""
DESAFIO 096

Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.
"""
def area(a,b):
    soma = (a*b)
    print(f'A área de {a:.2f} X {b:.2f} terreno é {soma:.2f} m².')

#Programa Principal
area (float(input('Digite a largura (m²): ')), float(input('Digite o comprimento (m²): ')))