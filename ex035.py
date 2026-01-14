#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')