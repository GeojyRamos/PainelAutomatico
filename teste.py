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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["WDM_SSL_VERIFY"] = "0"
warnings.simplefilter("ignore", category=urllib3.exceptions.InsecureRequestWarning)  # Remove warnings do urllib3
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

    component2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(12) > div.css-1p0yltr > div.css-fwe93l > fieldset > div > div:nth-child(2) > div > div > div:nth-child(3)")))
    if component2.is_displayed():
        component2.click()
    else:

        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(11) > div.css-1p0yltr > div.css-fwe93l > fieldset > div > div:nth-child(2) > div > div > div:nth-child(3)").click()

    component3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(12) > div.css-1p0yltr > div.css-fwe93l > div > div > div > button")))
    component3.click()

    component4 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#reactRoot > div.grafana-app > div > div.css-1bgjk0t > div > div.css-1ntsjus-NavToolbar-actions > button:nth-child(1)")))
    component4.click()
    driver.execute_cdp_cmd("Emulation.setScriptExecutionDisabled", {"value": False})
    driver.execute_script("document.documentElement.requestFullscreen();")
    time.sleep(300)

except:
    print("Ocorreu um erro... Ao Acessar o Link do Grafana2")
    time.sleep(300)
    sys.exit()











