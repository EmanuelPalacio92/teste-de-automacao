# !!! Antes de começar, tenha certeza de ter o Selenium e o WebDriver instalados !!!
# 1 - pip install selenium
# 2 - pip install webdriver-manager
# 3 - pip install pyautogui  ->  Serve para controlar o cursor do mouse!

# Importar o pyautogui
import pyautogui


from selenium import webdriver # Importar a biblioteca Selenium
from webdriver_manager.firefox import GeckoDriverManager # Importar a biblioteca WebDriver-Manager do FireFox
from selenium.webdriver.firefox.service import Service # Executar navegador através do Drive Manager
# !!! Sempre que for utilizar uma automação com o Selenium, o código acima será exatamente o mesmo !!!

servico = Service(GeckoDriverManager().install()) # Identificar a versão do navegador atual e instalar o GeckoDrive correspondente a versão atual
navegador = webdriver.Firefox(service=servico) # Configurar o navegador para usar a versão do GeckoDriver
navegador.get("https://sige.seduc.ce.gov.br/") # Abrir em um site específico

# Navegar com a tecla TAB e acessar a aba acadêmico
pyautogui.press('tab') # Apertar a tecla TAB
pyautogui.press('tab') # Apertar a tecla TAB
pyautogui.press('enter') # Apertar a tecla ENTER

# Selecionar MUNICÍPIO
# pyautogui.click('apertar.png')


# Inserir login
pyautogui.press('tab') # Apertar a tecla TAB

# Encontrar qualquer elemento dentro da página (Todo elemento de um site tem um xpath por trás dele)
# navegador.find_element('xpath','/html/body/div/div/div[2]/div/div/div[1]/div[1]/div/a/div').click() # Clicar no Botão "ACADEMICO"


# Encontrar qualquer elemento dentro da página (Todo elemento de um site tem um xpath por trás dele)
# Clicar no opção "MUNICIPIO"
# navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/span/input[2]').click()
