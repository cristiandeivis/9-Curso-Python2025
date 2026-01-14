"""
DESAFIO 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

lista =[]
maior = 0
for c in range (5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado na posição {len(lista)-1} ')
    else:
        if valor > max(lista):
            lista.append(valor)
            print(f'O valor {valor} foi adicionado na posição {len(lista)-1} ')
        else:
            for c in range(0,len(lista)):
                if valor > lista[c]:
                    continue
                else:
                    lista.insert(c,valor)
                    print(f'O valor {valor} foi adicionado na posição {c} ')
                    break
    print (lista)