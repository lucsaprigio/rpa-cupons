import psutil
import ctypes
import pyautogui
import time

def click_imagem_especifica(caminho_imagem, timer):
        if timer > 0:
            while True:
                try:
                    pyautogui.locateOnScreen(caminho_imagem, confidence=0.8)
                    break
                except pyautogui.ImageNotFoundException:
                    time.sleep(timer)

        x, y, largura, altura = pyautogui.locateOnScreen(caminho_imagem, confidence=0.8)
        pyautogui.click(x + largura / 2, y + altura / 2)
        return

def verificar_processo(nome_processo, timeout=10):
     for _ in range(timeout):
          for processo in psutil.process_iter(['name']):
               if processo.info['name'] == nome_processo:
                    return True
          time.sleep(1)
     return False

def trazer_janela_para_frente(nome_processo):
    """Traz a janela do processo para frente."""
    user32 = ctypes.windll.user32
    for processo in psutil.process_iter(['pid', 'name']):
        if processo.info['name'] == nome_processo:
            hwnd = user32.FindWindowW(None, None)  # Procura a janela
            if hwnd:
                user32.SetForegroundWindow(hwnd)  # Traz a janela para frente
            break

def emitir_cupom(cod_produto):
    pyautogui.write(str(cod_produto))
    pyautogui.press('enter')
    pyautogui.press('F2')

    for _ in range(2):
        pyautogui.press('enter')
            
    pyautogui.write('1')

    for _ in range(5):
        pyautogui.press('enter')
    time.sleep(3)