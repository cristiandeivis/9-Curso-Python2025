"""Exercício 62:
elhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos.
Este abaixo foi feito por mim.
"""

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
opt = 1
c = 0
while c < 10:
        print (termo,end = ' ')
        termo = termo+razao
        c +=1
while opt != 0:
    opt = int(input('Quantos termos você quer mostrar mais? '))
    c = 1
    while c <= opt:
        print(termo, end = ' ')
        termo = termo+razao
        c+=1
