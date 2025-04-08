from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def abrirzabbix (options, link):
    # Inicializa o WebDriver com o perfil especificado
    drive = webdriver.Firefox(options=options)
    wait = WebDriverWait(drive,5)
    drive.get(link)
    try:
        #Verifica se não existe login, se não existir loga
        if(drive.current_url == "http://10.6.55.124/zabbix/"):
            drive.find_element(By.NAME, "name").send_keys("digital.expresso")
            drive.find_element(By.NAME, "password").send_keys("QsHXAiMzS&qM" + Keys.ENTER)

        #Minimiza a pagina assim que carregar o titulo da pagina
        if(wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-title-general']")))):
            drive.minimize_window()
            return drive
    except NoSuchElementException:
        print("Erro ao abrir o ZABBIX")
