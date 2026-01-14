"""DESAFIO 083

Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
lista = []
expressao = str(input('Digite sua expressão: '))
for c in range (len(expressao)):
    lista.append(expressao[c])
vabre = 0
vfecha = 0
erro = 0
for c in range (len(lista)):
    if lista[c] == '(':
        vabre += 1     
    if lista[c] == ')':
        vfecha += 1           
    if vfecha > vabre:
        erro = 1
if vabre - vfecha == 0 and erro == 0:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')