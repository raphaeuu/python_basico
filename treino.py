import pyautogui
import time
import subprocess


def abrir_Windows():
    pyautogui.press('win')
    print('Barra de pesquisa aberta.')

def abrir_bloco_notas():
    pyautogui.write('bloco de notas', interval= 0.1)
    pyautogui.press('enter')
    time.sleep(1)

# def criar_arquivo():
#     pyautogui.hotkey

# def criar_arquivo_novo():
#     pyautogui.hotkey('ctrl', 'n')
#     print('Arquivo criado.')
#     time.sleep(2)


def escrever_nome():
    pyautogui.write('Seja bem vindo, Raphael! Escreva abaixo. ')
    print('Texto inserido.')
    time.sleep(1)

def salvar_arquivo():
    pyautogui.press('archive')
    pyautogui.press('enter')

abrir_Windows()
abrir_bloco_notas()
# criar_arquivo_novo()
escrever_nome()
