#Programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessária
#sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Digite a Largura: '))
altura = float(input('Digite a Altura: '))
area= largura * altura
tinta = area/2
print(f'A área total é {area} m²')
print(f'A Quantidade de tinta necessária é {tinta:.2f} litros')
        
