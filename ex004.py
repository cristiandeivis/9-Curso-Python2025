#Fazer um programa que leia um dado e indique se:
#é numero, alfabético, maiúscula, minúscula, ou capitalizado (maíscula e minúscula).

dado = input('Digite algo: ')
print('É Numérico?', dado.isnumeric())
print('É Alfabético?', dado.isalnum())
print('É Maiúscula', dado.isupper())
print('É Minúscula', dado.islower())
print('É Capitalizado (maíúscula e minúscula)?', dado.istitle())