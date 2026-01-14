"""
DESAFIO 098

Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.


"""
from time import sleep
def contador(a,b,c):
    print()
    print (f'A contagem é de {a} até {b} com passo em {c}')
    cont = a
    if cont <= b:
        while cont <= b:
            print (cont, end = ' ', flush=True)
            sleep(0.5)
            cont += c
        print('Fim')
    else:
        while cont >= b:
            print (cont, end = ' ', flush=True)
            sleep(0.5)
            cont += c
        print('Fim')
contador(1,10,1)
contador(10,0,-2)
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a,b,c)