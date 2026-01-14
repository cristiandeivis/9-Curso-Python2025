#Programa que lê quanto uma pessoa tem em Reais e
#quantos dólares ela pode comprar

n = float(input('Digite um valor em R$ '))
conv = float(n/5.33)
print(f'O valor em dólares que você teria é {conv:.2f}')
