"""Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso de zero até
20

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostra-lo por extenso."""

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze',
           'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    opt = int(input('digite um número de 0 a 20: '))
    if opt < 0 or opt > 20:
        print('Número incorreto, digite novamente.')
    else:
        print (f'O número digitado foi {numeros[opt]}')