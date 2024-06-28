print("\n")
print("ｓａｂｏｒ ｅｘｐｒｅｓｓ\n")
print("Bem vindo ao nosso restaurante! O que deseja?\n")


nome_usuario = input("Qual o seu nome? ")
print("\n")

print("1. Cadastrar restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

opcao_escolhida = int(input(f'{nome_usuario}, escolha uma opção: '))


if opcao_escolhida == 1:
    print('Cadastar restaurante.')
elif opcao_escolhida == 2:
    print("Listar restaurante.")
elif opcao_escolhida == 3:
    print("Ativar restaurante.")
else:
    print("Encerrando o programa!")