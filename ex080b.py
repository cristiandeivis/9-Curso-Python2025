"""
DESAFIO 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista = []
for c in range (0,5):
    print (lista)
    numero = int(input('Digite um Número: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f'O número {numero} foi inserido na última posição')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos,numero)
                print(f'O número foi inserido na posição {pos}')
                break
            pos +=1
print (lista)