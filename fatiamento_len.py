# variavel = 'Olá, mundo!'
# print(variavel[0:11])
# print(len(variavel[3]))

nome_usuario = input('Digite seu nome: ')
idade_usuario = int(input('Digite sua idade: '))

if nome_usuario and idade_usuario:
    print(f'Seu nome é: {nome_usuario}')
    print(f'Seu nome invertido é: {nome_usuario[::-1]}')

    if ' ' in nome_usuario:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços.')

    print(f'Seu nome tem ({len(nome_usuario)}) letras')
    print(f'A primeira letra do seu nome é ({nome_usuario[0]})')
    print(f'A última letra do seu nome é ({nome_usuario[-1:]})')
else:
    print('Desculpe, você deixou campos vazios. Tente novamente!')