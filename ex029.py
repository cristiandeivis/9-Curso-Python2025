#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80K/h mostrar
#uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km a mais

vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel-80)*7
    print(f'Você foi multado em R$ {multa:.2f}')
else:
    print('Você não foi multado')