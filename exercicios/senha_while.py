# Criar login e senha de usuário
criacao_login = input('Crie seu login: ')
criacao_senha = input('Crie sua senha (apenas números): ')
print('\n')

# Variáveis de login
tentativa = 0
login = ''
senha = ''

max_tentativas = 3

while tentativa < max_tentativas:

    login = input('Login: ')
    senha = input('Senha: ')
    print('\n')

    if login == criacao_login and senha == criacao_senha:
       print(f'Bem vindo, {criacao_login}')
       print('Login realizado com sucesso!')
       break
    else:
        tentativa += 1
        print(f'Usuário ou senha incorretos. Tentativa ({tentativa}) de ({max_tentativas}).')
    
if tentativa == max_tentativas:
    print('Número máximo de tentativas atingido. Tente novamente!')

