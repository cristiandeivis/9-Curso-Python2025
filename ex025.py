#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite o seu nome completo: ')).strip()
nome_minuscula = nome.lower()
print ('silva' in nome_minuscula)