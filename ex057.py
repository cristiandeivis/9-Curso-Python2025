"""Exercício 57:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor correto."""


sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in ('MmFf'):
    sexo = str(input('Sexo incorreto, digite novamente: ')).upper().strip()[0]
print (f'Agora sim, o sexo é {sexo}')