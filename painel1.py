from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def abrirPainel1 (options, link):
    # Inicializa o Webdriver com o perfil especificado
    driver = webdriver.Firefox(options=options)
    driver.set_window_position(2000,0)
    driver.fullscreen_window()
    wait = WebDriverWait(driver,5)
    driver.get(link)

    try:
        #Verifica se não existe login, se não existir loga
        if(wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=':r0:']")))):            
            if (driver.current_url == "http://10.6.55.124:3000/login"):
                driver.find_element(By.NAME, "user").send_keys("grafana")
                driver.find_element(By.NAME, "password").send_keys("grafana" + Keys.ENTER)

        #Clica no botão Start Playlist TV1
        try:  
            component = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/main/div[3]/div/div/div[2]/ul/li[1]/div/div/button")))
            component.click()
        except TimeoutException:
            component = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div[3]/div/div[1]/div/div[2]/ul/li[1]/div/div/button")))
            component.click()

        #Seleciona o modo de visualização Kiosk
        try: 
            component = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='option-true-radiogroup-1']")))
            component.click()
        except TimeoutException:
            component = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='option-true-radiogroup-3']")))
            component.click()

        #Iniciar o Painel clicando no botão Start TV1
        try:
            component = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/button")))
            component.click()
        except TimeoutException:
            component = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/button")))
            component.click()
        
        #Colocar tela cheia
        driver.fullscreen_window()

        return driver

    except NoSuchElementException:
        print("Erro no Painel 1.")

