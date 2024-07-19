"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Exercício 1

try:
    nome_user = input('Insira seu nome: ')
    numero_user = int(input(f'{nome_user}, insira um número: ')) %2

    if numero_user == 0:
        print(f'{nome_user}, seu número é par!')
    else:
        print(f'{nome_user}, seu número é ímpar!')
except ValueError:
    print('Erro: Tente novamente inserindo um valor de número inteiro.')