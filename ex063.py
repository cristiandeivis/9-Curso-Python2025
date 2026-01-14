"""Exercício 63:
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8.
Meu exercício
"""
n = int(input('Quantos termos você quer mostrar? '))
c = 0
valor = 0
ant = 0
post = 1
while c < n:
    print (valor, end = ' → ')
    ant = valor + post
    valor = post
    post = ant 
    c+=1
    


    
        