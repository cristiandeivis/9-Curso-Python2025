#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
print("""Digite [1] para converter em Binário
Digite [2] para converter em Octal
Digite [3] para converter em Hexadecimal""")
opcao = int(input('>>> '))
if opcao == 1:
    print(f'O valor de {numero} em Binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O valor de {numero} em Octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O valor de {numero} em Hexadecimanl é {hex(numero)[2:]}')
else:
    print('Opção Inválida!') 