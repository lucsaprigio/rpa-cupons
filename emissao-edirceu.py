import pyautogui
import time
import subprocess
import random
from tkinter import Tk, messagebox
from utils import click_imagem_especifica, verificar_processo, trazer_janela_para_frente, emitir_cupom

root = Tk()
root.withdraw()

lista_produtos = [
     87,
     89, 
     21,
     419,
     519   
]

lista_lancados = []

sys_26 = r"C:\gc\sys_026.exe"

subprocess.Popen(sys_26)

if verificar_processo("sys_026.exe"):
     trazer_janela_para_frente("sys_026.exe")
     time.sleep(3)
else:
     messagebox.showerror("Erro", "O sistema não foi iniciado.")
     exit()

pyautogui.PAUSE = 1

pyautogui.alert('Clique em "OK" para começar.')
time.sleep(1)

click_imagem_especifica('campo-senha.png', 0)

pyautogui.write('#2025#')

pyautogui.press('enter')

pyautogui.press('enter')

click_imagem_especifica('cupom-eletronico.png', 2)

pyautogui.press('enter')

codigo = random.choice(lista_produtos)

lista_lancados.append(codigo)

while len(lista_lancados) < 20: 
    # emissão dos cupons

    emitir_cupom(codigo)

