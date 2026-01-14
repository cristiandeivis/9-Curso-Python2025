#Crie um programa que leia o nome de uma cidade e diga se ela
#começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ').strip())
print(cidade[:5].upper() == 'SANTO') #vai pegar até a 5ª posição e ver se é igual a santo em maiúscula.