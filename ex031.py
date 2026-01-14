#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#E R$0,45 para viagens mais longas.

dist = int(input('Digite a distancia em km: '))
if dist <= 200:
    valor = dist*0.50
    print (f'O valor da viagem foi de R$ {valor:.2f}')
else:
    valor = dist*0.45
    print(f'O valor da sua viagem foi de R$ {valor:.2f}')