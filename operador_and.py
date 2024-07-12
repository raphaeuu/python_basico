entrada = input('[E] Entrar [S] Sair: ')
senha_digitada = input('Insira a senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou!')
else:
    print('Você saiu!')

