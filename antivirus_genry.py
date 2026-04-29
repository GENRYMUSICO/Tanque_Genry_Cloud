import pystray
from PIL import Image, ImageDraw
import webbrowser
import threading
import time
import os
import psutil
import pyttsx3
import requests 
import ctypes
import datetime
import base64
import sys
import shutil
import subprocess
import random

# --- 1. CONFIGURACIÓN DE IDENTIDAD Y NUBE ---
TOKEN_GH = "TU_TOKEN_AQUI" 
USUARIO_GH = "GENRYMUSICO"
REPO_GH = "Tanque_Genry_Cloud_Peru"

NOMBRE_APP = "Antivirus Genry V1.285 - MADE IN PERÚ"
FONETICA_NOMBRE = "Yenry Núñez"

# --- 2. BÚNKER MUSICAL (REPERTORIO ACTUALIZADO) ---
PLAYLIST_GENRY = [
    "https://www.youtube.com/watch?v=HNwqRXGtvLA", # El Marciano
    "https://www.youtube.com/watch?v=cDZjjcl8Yrg", # Mix Oficial Gency
    "https://www.youtube.com/watch?v=LJSCBid9Szc", # Mix Geniales Live
    "https://www.youtube.com/watch?v=tfio0Un3fQs", # Mix Natusha
    "https://www.youtube.com/watch?v=OhsEGS6ZPQE"  # Technocumbias
]

# --- 3. FUNCIONES DE SOPORTE TÉCNICO ---

def hablar(texto):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.say(texto)
        engine.runAndWait()
    except: pass

def obtener_adn_maquina():
    try:
        placa = subprocess.check_output("wmic baseboard get serialnumber", shell=True).decode().split('\n')[1].strip()
        uuid = subprocess.check_output("wmic csproduct get uuid", shell=True).decode().split('\n')[1].strip()
        return f"PLACA:{placa} | UUID:{uuid}"
    except: return "HARDWARE_DESCONOCIDO"

def enviar_a_la_fiscalia(detalle):
    if TOKEN_GH == "TU_TOKEN_AQUI": return
    fecha_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    adn = obtener_adn_maquina()
    url = f"https://api.github.com/repos/{USUARIO_GH}/{REPO_GH}/contents/EVIDENCIA_POLICIA/REPORTE_{fecha_id}.txt"
    reporte = f"EXPEDIENTE FORENSE\nFECHA: {fecha_id}\nDETALLE: {detalle}\nHARDWARE: {adn}"
    contenido_b64 = base64.b64encode(reporte.encode()).decode()
    headers = {"Authorization": f"token {TOKEN_GH}", "Accept": "application/vnd.github.v3+json"}
    payload = {"message": f"Evidencia {fecha_id}", "content": contenido_b64}
    try: requests.put(url, headers=headers, json=payload, timeout=10)
    except: pass

# --- 4. LÓGICA MUSICAL (EL JALÓN) ---

def jalar_exito_aleatorio(icon=None, item=None):
    cancion = random.choice(PLAYLIST_GENRY)
    webbrowser.open(cancion)
    hablar("Cambiando el paso. Escucha otro éxito del Grupo Genry.")

# --- 5. INTERFAZ Y PATRULLA ---

def crear_icono_rayo_izquierda():
    img = Image.new('RGB', (64, 64), color=(0, 0, 139))
    d = ImageDraw.Draw(img)
    # Rayo apuntando a la izquierda (Ataque total)
    d.polygon([(40,5), (55,28), (38,28), (50,48), (14,35), (26,35)], fill=(255, 215, 0))
    return img

def iniciar_tray():
    """Interfaz del Tray con máxima compatibilidad de versión"""
    try:
        # Definimos los ítems primero
        items_menu = [
            pystray.MenuItem("🎵 REPRODUCIR GRUPO GENRY", lambda i, n: jalar_exito_aleatorio()),
            pystray.MenuItem("⏭️ JALAR OTRO ÉXITO (Flecha)", jalar_exito_aleatorio),
            pystray.Menu.SEPARATOR, # <--- Cambio de estrategia: Usamos la constante interna
            pystray.MenuItem("📖 MANUAL DE CAZA", lambda i, n: print("Abriendo Manual...")),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("❌ CERRAR TANQUE", lambda i, n: i.stop())
        ]
        
        menu = pystray.Menu(*items_menu)
        icon = pystray.Icon("Genry", crear_icono_rayo_izquierda(), NOMBRE_APP, menu)
        icon.run()
    except Exception as e:
        # Si pystray sigue renegando con el separador, lanzamos el menú sin rayas
        print(f"\033[1;33m[AVISO TRAY]\033[0m Reajustando interfaz por compatibilidad...")
        menu_simple = pystray.Menu(
            pystray.MenuItem("🎵 REPRODUCIR GRUPO GENRY", lambda i, n: jalar_exito_aleatorio()),
            pystray.MenuItem("⏭️ JALAR OTRO ÉXITO (Flecha)", jalar_exito_aleatorio),
            pystray.MenuItem("❌ CERRAR TANQUE", lambda i, n: i.stop())
        )
        icon = pystray.Icon("Genry", crear_icono_rayo_izquierda(), NOMBRE_APP, menu_simple)
        icon.run()

def patrulla_total():
    while True:
        if ctypes.windll.kernel32.IsDebuggerPresent(): sys.exit()
        # Aquí va la lógica de vigilancia de procesos y red que ya tenemos...
        time.sleep(1)

# --- 6. ARRANQUE DEL BÚNKER ---

if __name__ == "__main__":
    if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(NOMBRE_APP)
    print(f"\033[1;34m--- {NOMBRE_APP} ---\033[0m")
    print(f"\033[1;32m[SISTEMA]\033[0m Identidad de Hardware: {obtener_adn_maquina()}")
    
    # Iniciar procesos
    threading.Thread(target=iniciar_tray, daemon=True).start()
    threading.Thread(target=patrulla_total, daemon=True).start()
    
    hablar(f"Sistema {FONETICA_NOMBRE} iniciado. Hardware identificado. Disfruta la música, Comandante.")
    
    while True: time.sleep(1)
