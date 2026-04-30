import time
import os
import subprocess
import sys

# Nombre del archivo principal del antivirus
ANTIVIRUS_SCRIPT = "antivirus_genry.py"

def vigilar_tanque():
    while True:
        # Verificamos si el proceso del antivirus está corriendo
        # Si no lo encuentra, lo vuelve a lanzar en silencio
        salida = subprocess.check_output('tasklist', shell=True).decode()
        if "python" in salida.lower() and ANTIVIRUS_SCRIPT.lower() in salida.lower():
            pass
        else:
            # Si el tanque cayó, lo resucitamos
            subprocess.Popen([sys.executable, ANTIVIRUS_SCRIPT])
        
        time.sleep(2) # Verifica cada 2 segundos

if __name__ == "__main__":
    vigilar_tanque()
