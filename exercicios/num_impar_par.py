usuario = input('Qual seu nome? ')
num_usuario = int(input(f'{usuario}, escolha um número:'))
num = num_usuario % 2

if num == 0:
    print(f'{usuario}, esse número é par!')
else:
    print(f'{usuario}, esse número é ímpar!')