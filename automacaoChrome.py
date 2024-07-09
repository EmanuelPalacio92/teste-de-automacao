# Importar a biblioteca Selenium
from selenium import webdriver
# Importar a biblioteca WebDriver-Manager
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

# Sempre que for utilizar uma automação com o Selenium, o código acima será exatamente o mesmo!

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://censobasico.inep.gov.br/censobasico/#/")



