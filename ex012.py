#Algorítmo que lê o preço de um produto e mostra seu novo preço
#com 5% de desconto

preco = float(input('Digite o Preço em R$ '))
npreco = float(preco*5)/100

print(f'O preço do produto com 5% de desconto  é {preco-npreco:.2f}')
