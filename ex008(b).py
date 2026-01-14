#Complemento do exercício anterior criar um algoritmo que lê um valor em metros
#e o exibe convertido em Km, Hectômetro, Decâmetro, centímetro e milímetro.

metro = float(input('Digite o valor em metros: '))
km  = metro/1000
hm = metro/100
dc = metro/10
cm = metro*100
mm = metro*1000

print (f'A medida de {metro} corresponde a: ')
print (f'{km} quilômetros.')
print(f'{hm} hectômetros.')
print(f'{dc} decâmetros.')
print(f'{cm} centrímetros.')
print(f'{mm} milímetros.')
