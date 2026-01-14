"""Desafio 089

Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

notas =[]
while True:
    nome = input('Digite o nome do aluno: ').lower().strip().capitalize()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1+nota2)/2
    notas.append([nome,[nota1, nota2], media])
    opt = str(input('Deseja Continuar [S/N]: '))
    if opt in 'Nn':
        break
print('=-'*30)
print (notas)
print('Nº   Nome:         Nota 1         Nota 2         Média')
for c in range (len(notas)):
    print (f'{c:<5}{notas[c][0]:<15}{notas[c][1][0]:<15.2f}{notas[c][1][1]:<15.2f}{notas[c][2]:<15.2f}', end = ' ')
    print()
print('=-'*30)
while True:
    num = int(input('Mostrar notas de qual aluno? '))
    print('=-'*30)
    print('Nº   Nome:         Nota 1         Nota 2         Média')
    print (f'{num:<5}{notas[num][0]:<15}{notas[num][1][0]:<15.2f}{notas[num][1][1]:<15.2f}{notas[num][2]:<15.2f}', end = ' ')
    print()
    print('=-'*30)
    opt = str(input('Deseja Continuar [S/N]: '))
    if opt in 'Nn':
         break
print('=-'*30)
