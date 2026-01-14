#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
print(f'A hipotenusa é {hypot(cato,cata):.2f}')