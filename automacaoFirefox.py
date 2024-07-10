# !!! Antes de começar, tenha certeza de ter o Selenium e o WebDriver instalados !!!
# 1 - pip install selenium
# 2 - pip install webdriver-manager
# 3 - pip install pyautogui  ->  Serve para controlar o cursor do mouse!

login = input("Digite seu usuário ")
senha = input("Digite sua senha ")

# Importar o pyautogui
import pyautogui
import time

from selenium import webdriver # Importar a biblioteca Selenium
from webdriver_manager.firefox import GeckoDriverManager # Importar a biblioteca WebDriver-Manager do FireFox
from selenium.webdriver.firefox.service import Service # Executar navegador através do Drive Manager
# !!! Sempre que for utilizar uma automação com o Selenium, o código acima será exatamente o mesmo !!!



servico = Service(GeckoDriverManager().install()) # Identificar a versão do navegador atual e instalar o GeckoDrive correspondente a versão atual
navegador = webdriver.Firefox(service=servico) # Configurar o navegador para usar a versão do GeckoDriver
navegador.get("https://sige.seduc.ce.gov.br/") # Abrir em um site específico


time.sleep(2)
pyautogui.press('tab') # Apertar a tecla TAB
pyautogui.press('tab') # Apertar a tecla TAB
pyautogui.press('enter') # Apertar a tecla ENTER


time.sleep(2)
pyautogui.keyDown('shift')
pyautogui.press('tab')
pyautogui.keyUp('shift')
pyautogui.press(['left','tab'])
pyautogui.write(login)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')

time.sleep(3)
pyautogui.press(['tab','tab','tab','tab','tab','tab','tab',])
pyautogui.press('enter')

time.sleep(3)
pyautogui.press(['tab','tab'])
pyautogui.write('23250976')
pyautogui.press(['down','enter','tab','enter'])


# Encontrar qualquer elemento dentro da página (Todo elemento de um site tem um xpath por trás dele)
# navegador.find_element('xpath','/html/body/div/div/div[2]/div/div/div[1]/div[1]/div/a/div').click() # Clicar no Botão "ACADEMICO"


# Encontrar qualquer elemento dentro da página (Todo elemento de um site tem um xpath por trás dele)
# Clicar no opção "MUNICIPIO"
# navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/span/input[2]').click()


#navegador.find_element('xpath','/html/body/table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td[2]/a[1]/img').click()