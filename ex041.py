"""
DESAFIO 041

A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 20 anos: SÊNIOR
Acima: MASTER
"""

from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = (ano_atual-nascimento)
if idade <= 9:
    print(f'Você tem {idade} anos então é da categoria: \033[0;31;40mMirim\033[m')
elif idade <= 14:
    print(f'Você tem {idade} anos então é da categoria: \033[0;31;40mInfantil\033[m')
elif idade <= 19:
    print(f'Você tem {idade} anos então é da categoria: \033[0;31;40mJúnior\033[m')
elif idade <= 20:
    print(f'Você tem {idade} anos então é da categoria: \033[0;31;40mSênior\033[m')
else:
    print(f'Você tem {idade} anos então é da categoria: \033[0;31;40mMaster\033[m')