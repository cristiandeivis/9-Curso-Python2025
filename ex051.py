"""
Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final mostre os 10 primeiros termos dessa progressão
"""
termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
for c in range (10):
        print(termo)
        termo += razao