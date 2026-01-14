"""
DESAFIO 043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a 
tabela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida
"""
peso = float(input('Digite o seu peso: ').replace(',', '.'))
altura = float(input('Digite sua altura: ').replace(',', '.'))
IMC = peso/(altura**2) #altura ao quadrado
print (f'Seu IMC é {IMC:.2f}')
if IMC < 18.5:
    print ('Você está abaixo do peso!')
elif 18.5 <= IMC < 25:
    print ('Você está no peso normal!')
elif 25 <= IMC < 30:
    print ('Você está com Sobrepeso!')
elif 30 <= IMC < 40:
    print ('Você está com Obesidade!')
elif IMC >= 40:
    print ('Você está com Obesidade Mórbida!')
