"""Crie um programa que tenha uma tupla com várias palavras(não
usar acentos). Depois disso, você deve mostrar para cada palavra
quais são suas vogais"""

lista = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for palavras in lista:
    print (f'\nNa palavra {palavras} temos as vogais: ', end =' ')
    for letras in palavras:
        if letras.lower() in ('a,e,i,o,u'):
           print (letras, end = ' ')