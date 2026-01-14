"""
DESAFIO 040
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""
from math import floor
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print(f'Sua média é {media:.2f} e você está reprovado!')
elif media <= 6.99:
    print(f'Sua média é {media:.2f} e você está em recuperação')
else:
    print(f'Parabéns você está com a média {media:.2f} e foi aprovado!')