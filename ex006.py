#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))
dobro = numero*2
triplo = numero*3
raizquadrada = numero**(1/2)
print('O número é: {} \nSeu dobro é: {} \nSeu triplo é: {} \nSua raiz é: {:.2f}'.format(numero,dobro,triplo,raizquadrada))
