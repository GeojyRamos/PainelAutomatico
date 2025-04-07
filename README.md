# PainelAutomatico
Automação para abrir o painel de monitoramento de GEITS

✅ Gerar um executável com PyInstaller
-Instale o PyInstaller:
  pip install pyinstaller
  
-Gere o executável com:
  pyinstaller --onefile --windowed abrir_chrome.py 
  
  --onefile: empacota tudo em um único .exe
  --windowed: não abre janela de terminal (ideal para apps com interface gráfica ou sem log no console)

O executável estará em: dist/main.exe
