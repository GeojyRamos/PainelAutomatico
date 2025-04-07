import sys
import os
from cx_Freeze import setup, Executable

sys.setrecursionlimit(5000)  # Evita erro de recursão

# Dependências
build_exe_options = {
    "packages": ["sys", "os", "selenium", "time", "warnings", "getpass", "urllib3"],
    "excludes": ["tkinter"],  # Remove pacotes desnecessários
    "include_files": [],  # Adicione arquivos adicionais aqui, se necessário
}

# Configuração do executável
setup(
    name="PainelAutomatico",
    version="1.0",
    description="Automação com Selenium",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None)],
)