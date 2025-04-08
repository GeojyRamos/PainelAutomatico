import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
   
def abrirPainel2 (link):
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "chrome")
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    options.add_experimental_option("detach", True) 
    options.add_experimental_option("excludeSwitches", ['enable-automation']);
    options.add_argument(r"user-data-dir={}".format(profile))
    options.add_argument("--remote-debugging-port=9222")  # Habilita o debugging remoto

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver,5)

    driver.get(link)

    #Verifica se não existe login, se não existir loga
    if (driver.current_url == "http://10.6.55.124:3000/login"):
        if(wait.until(EC.presence_of_element_located((By.NAME, "user")))):
            driver.find_element(By.NAME, "user").send_keys("grafana")
            driver.find_element(By.NAME, "password").send_keys("grafana" + Keys.ENTER)

    #Clica no botão Start Playlist TV2
    try:
        component1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pageContent']/div[3]/div/div/div[2]/ul/li[2]/div/div/button")))
        component1.click()
    except TimeoutException:
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div/button").click()
        print('Componente Tv2 não existe')

    #Seleciona o modo de visualização Kiosk
    try:
        component2 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='option-true-radiogroup-1']")))
        component2.click()
    except TimeoutException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/fieldset/div/div[2]/div/div/div[3]").click()
    
    #Desmarca Time
    try:
        component3 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/fieldset/div[3]/div[2]/div/div/div/label[1]/div/span")))
        component3.click()
    except TimeoutException:
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/fieldset/div[3]/div[2]/div/div/div/label[1]/div/span").click()

    #Iniciar o Painel clicando no botão Start TV2
    try:                                                                      
        component4 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div/button")))
        component4.click()
    except TimeoutException:
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div/button").click()

    return driver