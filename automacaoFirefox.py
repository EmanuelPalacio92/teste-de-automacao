# !!! Antes de começar, tenha certeza de ter o Selenium e o WebDriver instalados !!!
# 1 - pip install selenium
# 2 - pip install webdriver-manager

from selenium import webdriver # Importar a biblioteca Selenium
from webdriver_manager.firefox import GeckoDriverManager # Importar a biblioteca WebDriver-Manager do FireFox
from selenium.webdriver.firefox.service import Service # Executar navegador através do Drive Manager
# !!! Sempre que for utilizar uma automação com o Selenium, o código acima será exatamente o mesmo !!!

servico = Service(GeckoDriverManager().install()) # Identificar a versão do navegador atual e instalar o GeckoDrive correspondente a versão atual
navegador = webdriver.Firefox(service=servico) # Configurar o navegador para usar a versão do GeckoDriver
navegador.get("https://sige.seduc.ce.gov.br/") # Abrir em um site específico


# Encontrar qualquer elemento dentro da página (Todo elemento de um site tem um xpath por trás dele)
navegador.find_element('xpath','/html/body/div/div/div[2]/div/div/div[1]/div[1]/div/a/div').click() # Clicar no Botão "ACADEMICO"

