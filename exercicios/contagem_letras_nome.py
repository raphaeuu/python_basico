"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

#Exercício 3

try:
    nome_usuario = input('Insira seu nome: ')
    contagem_nome = len(nome_usuario)

    if contagem_nome <= 4:
        print(f'{nome_usuario}, seu nome é pequeno e contém ({contagem_nome}) letras.')
    elif contagem_nome >= 5 and contagem_nome <= 6:
        print(f'{nome_usuario}, seu nome é normal e contém ({contagem_nome}) letras.')
    elif contagem_nome > 6:
        print(f'{nome_usuario}, seu nome é muito grande e contém ({contagem_nome}) letras.')
    else:
        print('Insira apenas letras e tente novamente. ')
except ValueError:
    print('Erro: Informe apenas o nome. ')