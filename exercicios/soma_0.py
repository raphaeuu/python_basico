numero_somado = 0
numero_user = int(input("Insira um número: "))

#numero = int(input("Insira um número: "))

while numero_user != "Sair":     

    numero_somado += numero_user
    numero_user = int(input("Insira mais um número: "))
    print(f'Soma atual: {numero_somado + numero_user}.')

print(
    "------------------------------------------------------\n"
    "Você pressionou o número 0 (zero). Operação encerrada.\n"
    f"Soma total: {numero_somado}."
    )
