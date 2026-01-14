"""Crie um programa que leia uma frase e diga se ela é um
palíndromo, desconsiderando os espaços e acentos.
Exemplos:
- Apos a sopa 
- A sacada da casa 
- A torre derrota 
- O lobo ama o bolo
- Anotaram a data da maratona"""

frase = input('Digite uma frase: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
print (junto)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'A palavra é palíndromo')
else:
    print(f'A palavra não é palíndromo')
