import os

def exibir_nome_programa():
    print("ｓａｂｏｒ ｅｘｐｒｅｓｓ\n")

nome_usuario = input("Qual o seu nome? ")
print(f'Bem vindo ao nosso restaurante, {nome_usuario}! O que deseja?')

print("\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")
    

def finalizar_app():
    os.system('cls')
    print('Finalizando o app, obrigado!')

def escolher_opcao():
    opcao_escolhida = int(input(f'{nome_usuario}, escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastar restaurante.')
    elif opcao_escolhida == 2:
        print("Listar restaurante.")
    elif opcao_escolhida == 3:
        print("Ativar restaurante.")
    else:
        finalizar_app()

opcao_escolhida = int(input(f'{nome_usuario}, escolha uma opção: '))



def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()