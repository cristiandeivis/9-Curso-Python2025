#Faça um programa que leia uma frase pelo teclado e mostre:
#- Quantas vezes aparece a letra "A"
#- Em que posição ela aparece a primeira vez
#- Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
frase_minuscula = frase.lower()
print (f'A letra A aparece {frase_minuscula.count('a')} vez(es)')
print (f'A letra A aparece pela primeira vez na posição {frase_minuscula.find('a')+1} e pela última vez na posição {frase_minuscula.rfind('a')+1} ')