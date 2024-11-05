import string
import random


caracteres_minusculos_senha = string.ascii_lowercase
caracteres_maiusculos_senha = string.ascii_uppercase
numeros = string.digits
simbolos_esp = string.punctuation


criacao_login = input("Crie um usuário para acesso: ")
tamanho = int(input("Qual o tamanho da senha? "))

incluir_maiusculas_senha = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
incluir_numeros_senha = input("Incluir números? (s/n): ").lower() == 's'
incluir_simbolos_senha = input("Incluir símbolos? (s/n): ").lower() == 's'


caracteres = caracteres_minusculos_senha

if incluir_maiusculas_senha:
    caracteres += caracteres_maiusculos_senha
if incluir_numeros_senha:
    caracteres += numeros
if incluir_simbolos_senha:
    caracteres += simbolos_esp

login = criacao_login
senha_criada = ''.join(random.choice(caracteres) for _ in range(tamanho))
tentativa = 0

print(
    f"Seu login é: {login}"
    )   
print(
    f"Sua senha é: {senha_criada}"
    )

print('\n')
print('Insira os dados abaixo para efetuar login: ')


while True:
    login_input = input(
        "Login: "
        )
    senha_input = input(
        "Senha: ")

    if login_input != criacao_login:
        print(
            "Login incorreto. Tente novamente! ❌"
            )
        print("\n")
        tentativa += 1
        continue

    if senha_input != senha_criada:
        print(
            "Senha incorreta. Tente novamente! ❌" 
            )
        print("\n")
        tentativa += 1

    else:
        print(f"Seja bem vindo, {criacao_login}! ✅") 
        print("Redirecionando para página inicial.[■■■■■■■■■□] 99%... ")
        break


