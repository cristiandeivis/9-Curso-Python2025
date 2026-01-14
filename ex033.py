#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

if numero1 > numero2 and numero1 > numero3:
    print (f'O número maior é {numero1}')
if numero2 > numero1 and numero2 > numero3:
    print (f'O numero maior é {numero2}')
if numero3 > numero1 and numero3 > numero2:
    print (f'O numero maior é {numero3}')
#menor
if numero1 < numero2 and numero1 < numero3:
    print (f'O número menor é {numero1}')
if numero2 < numero1 and numero2 < numero3:
    print (f'O numero maior é {numero2}')
if numero3 < numero1 and numero3 < numero2:
    print (f'O numero maior é {numero3}')