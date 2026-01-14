#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input('Digite o Seu Nome Completo: ')
print (f'O Nome em Maiúsculas é: {nome.upper()}')
print (f'O Nome em Minúsculas é: {nome.lower()}')
print (f'O nome tem {len(nome)} caracteres.')
sem_espaco = (nome.replace(' ',''))
print (f'O nome tem {len(sem_espaco)} caracteres sem contar os espaços')
divisao = (nome.split())
print (f'O Primeiro Nome é: {divisao[0]}')
print (f'O primeirio nome tem {len(divisao[0])} letras')