#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite o Seu Nome Completo: ')).strip() #já vai remover espaços antes e depois
print (f'O Nome em Maiúsculas é: {nome.upper()}')
print (f'O Nome em Minúsculas é: {nome.lower()}')
print (f'O nome tem {len(nome) - nome.count(' ')} caracteres.') #vai diminuir os caracteres do nome menos a contagem de espaços.
print (f'O seu primeiro nome tem {nome.find(' ')} letras.') #ele procura a primeira posição do espaço então saberá quantas letrás há antes do espaço.