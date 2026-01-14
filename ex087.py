"""Desafio 087

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

pares = 0
soma = 0
maior = 0
lista = [[0,0,0],[0,0,0],[0,0,0]]
#Inclusão dos valores
for c in range (0,3):
    for d in range (0,3):
        lista[c][d] = int(input(f'Input: Digite um número na matriz {c} X {d+1}: '))
#Listagem e soma dos pares.
for c in range (0,3):
    for d in range (0,3):
        print(f'[{lista[c][d]:^4}]', end = '')
        if lista[c][d] % 2 == 0:
            pares += lista[c][d]
    print()
#Soma dos valores da terceira coluna
for c in range (0,3):
        soma += lista[c][2]
#Maior valor da segunda linha
for c in range (0,3):
        if c == 0:
            maior = lista[1][c]
        else:
            if lista[1][c] > maior:
                maior = lista[1][c]
print (f'A soma dos pares é {pares}')  
print (f'A soma dos valores da terceira coluna é {soma}')
print (f'O maior número da segunda linha é {maior}')

