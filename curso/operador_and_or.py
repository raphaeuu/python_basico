entrada = input('[E] Entrar [S] Sair: ')
senha_digitada = input('Insira a senha: ')
senha_permitida = '1234567'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
