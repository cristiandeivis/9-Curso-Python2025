#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#E R$0,45 para viagens mais longas.
dist = int(input('Digite a distancia em km: '))
calc = dist * 0.50 if dist <=200 else dist * 0.45
print (f'O custo da viagem é {calc:.2f}')