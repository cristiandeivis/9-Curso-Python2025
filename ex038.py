#DESAFIO 038
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
if num1 == num2:
    print ('Os números são iguais')
elif num1 > num2:
    print (f'O número {num1} é maior que o número {num2}')
else:
    print(f'O número {num2} é maior que o número {num1}')
