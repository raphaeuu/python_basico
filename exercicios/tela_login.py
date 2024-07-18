nome = input('Insira seu nome: ')
novo_usuario_login = input(f'{nome}, crie um novo login: ')
nova_senha_usuario = input(f'{nome}, crie uma nova senha: ')

print('\n')
print('Criação de credenciais realizada com sucesso!\n')

login_usuario = input('Insira seu login de usuário: ')
senha_usuario = input('Insira sua senha de login: ')
print('\n')

if login_usuario == novo_usuario_login:
    print('Login de usuário válido! Agora insira sua senha.\n')
else:
    print('Insira um login de usuário válido e tente novamente.')

if senha_usuario == nova_senha_usuario:
    print('Login efetuado com sucesso!')
    print('Aguarde o carregamento...')
    print('[■■■■■■■■■□] 99%...')
else:
    print('Insira uma senha com formato válido.')