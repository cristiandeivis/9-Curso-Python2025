#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o último nome separadamente
#Exemplo: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = str(input('Digite o seu nome completo: ')).strip()
divisao = nome.split()
count = len(divisao)
print (f'O primeiro nome é {divisao[0]} e o último nome é {divisao[count-1]}')