"""Crie um programa que tenha uma tupla com várias palavras(não
usar acentos). Depois disso, você deve mostrar para cada palavra
quais são suas vogais"""

palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for vogais in palavras:
    print (f'\nNa palavra {vogais} temos as vogais: ', end =' ')
    for c in range (0,len(vogais),1):
        if vogais[c] in ('A,E,I,O,U'):
           print (vogais[c], end = ' ')