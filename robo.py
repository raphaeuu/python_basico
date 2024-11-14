# import subprocess


# def abrir_calculadora():

#     try:
#         subprocess.Popen('calc')
#         print("Calculadora aberta com sucesso.")
#     except Exception as e:
#         print(f"Erro ao abrir a calculadora: {e}")



#         abrir_calculadora()


import pyautogui
import time
import subprocess
import random

def abrir_calculadora_com_pyautogui():

    pyautogui.press('win')
    time.sleep(2)

    pyautogui.write('Calculadora', interval=0.1)
    time.sleep(2)

    pyautogui.press('enter')
    print("Calculadora aberta com sucesso. ")

    subprocess.Popen('calc')
    time.sleep(2)

def realizar_operacao_aleatoria():
    numero1 = random.randint(1, 9)
    numero2 = random.randint(1, 9)

    operacao = random.choice(['+', '-', '*', '/'])

    for digito in str(numero1):
        pyautogui.press(digito)
        

    pyautogui.press(operacao)

    for digito in str(numero2):
        pyautogui.press(digito)
        pyautogui.press('enter')

    print(f"Operação realizada com sucesso! ({numero1} {operacao} {numero2})")

abrir_calculadora_com_pyautogui()
time.sleep(1)
realizar_operacao_aleatoria()