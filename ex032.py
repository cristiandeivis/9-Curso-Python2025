#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

#Ser divisível por 4.
#Não ser divisível por 100.
#Todo ano divisível por 400 é sempre bissexto.
#Ano bissexto inicia em 1582

ano = int (input ('Digite um ano a partir de 1582: '))
if ano >= 1582:
    if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 != 0)):
        print ('É bissexto')
    else:
        print('Não é bissexto')