nome_usuario = input('Qual o seu nome? ')
idade_usuario = int(input('Qual a sua idade? '))

if idade_usuario < 12:
    print(f'{nome_usuario}, você é criança!')
elif idade_usuario < 18:
    print(f'{nome_usuario}, você é adolescente!')
elif idade_usuario >= 18:
    print(f'{nome_usuario}, você é adulto!')
else:
    print('Insira uma idade válida e tente novamente.')
