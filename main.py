import getpass
import sys
import time
import os
import warnings
import urllib3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["WDM_SSL_VERIFY"] = "0"
warnings.simplefilter("ignore", category=urllib3.exceptions.InsecureRequestWarning)  # Remove warnings do urllib3
user = getpass.getuser()

# Caminho do perfil do Firefox
profile_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\06650nyo.FirefoxSelenium"

# Configurações do Firefox
options = Options()
options.set_preference("profile", profile_path)

# Inicializa o WebDriver com o perfil especificado
driver2 = webdriver.Firefox(options=options)

driver2.set_window_position(2000,0)
driver2.fullscreen_window()

wait = WebDriverWait(driver2,10)
try:
    driver2.get("http://10.6.55.124:3000/playlists")
    try:
        component = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=':r0:']")))
        if (driver2.current_url == "http://10.6.55.124:3000/login"):
            driver2.find_element(By.NAME, "user").send_keys("grafana")
            driver2.find_element(By.NAME, "password").send_keys("grafana" + Keys.ENTER)

        component = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/main/div/div/div[3]/div/div[1]/div/div[2]/ul/li[1]/div/div/button")))
        component.click()

        component = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/fieldset/div/div[2]/div/div/div[3]")))
        component.click()

        component = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div/button")))
        component.click()

        component = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-i9gxme > svg:nth-child(1)")))
        component.click()

        component = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.css-1chuu9v-toolbar-button:nth-child(1)")))
        component.click()

        driver2.fullscreen_window()

    except NoSuchElementException:
        print("Elemento não encontrado após a espera.")
except:
    print("Ocorreu um erro... Ao Acessar o Link do Grafana")
    sys.exit()

driver3 = webdriver.Firefox(options=options)
wait = WebDriverWait(driver3,10)
try:
    driver3.get("http://10.6.55.124/zabbix/")
    try:
        component = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='name']")))
        if(driver3.current_url == "http://10.6.55.124/zabbix/"):
            driver3.find_element(By.NAME, "name").send_keys("digital.expresso")
            driver3.find_element(By.NAME, "password").send_keys("QsHXAiMzS&qM" + Keys.ENTER)

        component = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='page-title-general']")))
        driver3.minimize_window()
    except NoSuchElementException:
        print("Elemento não encontrado após a espera.")
except:
    print("Ocorreu um erro... Ao Acessar o Link do ZABBIX")
    sys.exit()


user = getpass.getuser()
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "chrome")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation']);
options.add_argument(r"user-data-dir={}".format(profile))
options.add_argument("--remote-debugging-port=9222")  # Habilita o debugging remoto

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver,5)

try:
    driver.get("http://10.6.55.124:3000/playlists")

    if (driver.current_url == "http://10.6.55.124:3000/login"):
        component = wait.until(EC.presence_of_element_located((By.NAME, "user")))
        driver.find_element(By.NAME, "user").send_keys("grafana")
        driver.find_element(By.NAME, "password").send_keys("grafana" + Keys.ENTER)


    component1 = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pageContent']/div[3]/div/div[1]/div/div[2]/ul/li[2]/div/div/button")))
    if component1.is_displayed():

        component1.click()
    else:
        driver.find_element(By.XPATH,"//*[@id='pageContent']/div[3]/div/div[1]/div/div[2]/ul/li[1]/div/div/button").click()
        print('Componente Tv2 não existe')

    try:
        component2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(12) > div.css-1p0yltr > div.css-fwe93l > fieldset > div > div:nth-child(2) > div > div > div:nth-child(3)")))
        component2.click()
    except TimeoutException:
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/fieldset/div/div[2]/div/div/div[3]").click()

    try:
        component3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(12) > div.css-1p0yltr > div.css-fwe93l > div > div > div > button")))
        component3.click()
    except TimeoutException:
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div/div/button").click()


    component4 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#reactRoot > div.grafana-app > div > div.css-1bgjk0t > div > div.css-1ntsjus-NavToolbar-actions > button:nth-child(1)")))
    component4.click()
    driver.execute_cdp_cmd("Emulation.setScriptExecutionDisabled", {"value": False})
    driver.execute_script("document.documentElement.requestFullscreen();")
    time.sleep(300)

except:
    print("Ocorreu um erro... Ao Acessar o Link do Grafana2")
    time.sleep(300)
    sys.exit()


while (driver.window_handles and driver2.window_handles and driver3.window_handles):
    if (driver == None):
        driver2.close()
        driver3.close()
        sys.exit()
    elif(driver2 == None):
        driver.close()
        driver3.close()
        sys.exit()
    elif(driver3 == None):
        driver.close()
        driver2.close()
        sys.exit()














