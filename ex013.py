#Algorítmo que lê o salário de um funcionário e mostra o seu 
#novo salário com 15% de aumento

salario = float(input('Digite o seu salário em R$ '))
print(f'O salário com 15% de aumento é {salario+(salario*15/100):.2f}')
