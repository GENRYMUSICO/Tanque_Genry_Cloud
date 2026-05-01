import time
import os
import subprocess
import sys

# Nombre del archivo principal del antivirus
ANTIVIRUS_SCRIPT = "antivirus_genry.py"

def vigilar_tanque():
    while True:
        try:
            # Verificamos si el proceso del antivirus está corriendo
            salida = subprocess.check_output('tasklist', shell=True).decode()
            if "python" in salida.lower() and ANTIVIRUS_SCRIPT.lower() in salida.lower():
                pass
            else:
                # Si el tanque cayó, lo resucitamos en silencio
                subprocess.Popen([sys.executable, ANTIVIRUS_SCRIPT], 
                                 creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception as e:
            print(f"Error en vigilancia: {e}")
        
        time.sleep(2) # El pulso del Búnker

if __name__ == "__main__":
    vigilar_tanque()
