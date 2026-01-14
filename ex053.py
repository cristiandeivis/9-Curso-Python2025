"""Crie um programa que leia uma frase e diga se ela é um
palíndromo, desconsiderando os espaços e acentos.
Exemplos:
- Apos a sopa 
- A sacada da casa 
- A torre derrota 
- O lobo ama o bolo
- Anotaram a data da maratona"""

original = input('Digite uma frase: ')
frase = original.lower().strip().replace(' ', '')
print (frase)
tamanho = len(frase)
nova = ''
for c in range(tamanho-1,-1,-1):
    nova += frase[c]
if frase == nova:
    print (f'A palavra {original} ao contrário é {nova} e é palíndroma!')
else:
    print (f'A palavra {original} ao contrário é {nova} e não é palíndroma!')