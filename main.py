import getpass
import time
import sys
import os
import warnings
import urllib3
from painel1 import abrirPainel1
from zabbix import abrirzabbix
from painel2 import abrirPainel2
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

os.environ["WDM_SSL_VERIFY"] = "0"
warnings.simplefilter("ignore", category=urllib3.exceptions.InsecureRequestWarning)  # Remove warnings do urllib3

user = getpass.getuser()

# Caminho do perfil do Firefox
profile_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\06650nyo.FirefoxSelenium"

# Configurações do Firefox
options = Options()
options.set_preference("profile", profile_path)

driverPainel1 = abrirPainel1(options, "http://10.6.55.124:3000/playlists")
driverZabbix = abrirzabbix(options, "http://10.6.55.124/zabbix/")
driverPainel2 = abrirPainel2("http://10.6.55.124:3000/playlists")

while True:
    try:
        # tenta acessar as janelas de cada driver
        driverPainel1.window_handles
        driverZabbix.window_handles
        driverPainel2.window_handles
        time.sleep(20)

    except WebDriverException:
        # se qualquer driver estiver fechado, fecha os outros
        try:
            driverPainel1.quit()
        except:
            pass
        try:
            driverZabbix.quit()
        except:
            pass
        try:
            driverPainel2.quit()
        except:
            pass
        sys.exit()














