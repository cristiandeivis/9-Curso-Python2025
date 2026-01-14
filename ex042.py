"""
DESAFIO 042
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes
"""

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode formar um triângulo ', end='') #o end='' permite concatenar com o print antes do final do IF (em resumo não vai ter enter antes do fim da linha
    if a==b==c:
        print ('Equilátero')
    elif a!=b!=c!=a:
        print ('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não podem formar um triângulo')