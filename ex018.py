#Faça um programa que leia um ângulo qualquer e mostre o valor do seno
#cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
ang = float(input('Digite o Ângulo: '))
radians = radians(ang) #tem que converter pra radianos pra cacular certo
print (f'O valor do Seno é: {sin(radians):.2f}, \nO valor do Cosseno é {cos(radians):.2f} \n O valor da Tangente é: {tan(radians):.2f}')