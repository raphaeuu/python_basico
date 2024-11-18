import pyautogui
import time
import subprocess
import os

# def abrir_vscode_com_pyautogui():

#     try:
#         pyautogui.press('win')
#         time.sleep(2)

#         subprocess.Popen('code')
#         time.sleep(3)
#     except Exception as e:
#         print(f"Erro ao abrir o VS Code: {e}")
 
def criar_arquivo():
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

    pyautogui.write('hello_world.py', interval=0.1)
    print("Arquivo criado com sucesso no VS Code.")

    pyautogui.press('enter')

def digitar_script():
    pyautogui.write("print('Hello, World!')", interval=0.1)
    print('Frase inserida.')

def executar_arquivo():
    pyautogui.hotkey('ctrl', '`')
    time.sleep(1)

def abrir_terminal():
    try:
        caminho_arquivo = os.path.join(os.getcwd(), "hello_world.py")
        subprocess.run(["python", caminho_arquivo])
        print("Arquivo hello_world.py executado com sucesso!")
    except Exception as e:
        print(f"Erro ao executar o arquivo: {e}")
    

# abrir_vscode_com_pyautogui()
time.sleep(1)
criar_arquivo()
time.sleep(1)
digitar_script()
time.sleep(1)
executar_arquivo()
time.sleep(1)
abrir_terminal()