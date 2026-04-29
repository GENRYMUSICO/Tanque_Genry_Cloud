import pystray
from PIL import Image, ImageDraw, ImageFont
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
import subprocess
import random

# --- 1. CONFIGURACIÓN DE IDENTIDAD Y NUBE ---
TOKEN_GH = "TU_TOKEN_AQUI" # <--- PEGUE SU TOKEN AQUÍ PARA LOS REPORTES
USUARIO_GH = "GENRYMUSICO"
REPO_GH = "Tanque_Genry_Cloud"

NOMBRE_APP = "Antivirus Genry V1.315 - MADE IN PERÚ"
FONETICA_NOMBRE = "Yenry Núñez"

# --- 2. BÚNKER MUSICAL ---
PLAYLIST_GENRY = [
    "https://www.youtube.com/watch?v=HNwqRXGtvLA", # El Marciano
    "https://www.youtube.com/watch?v=cDZjjcl8Yrg", # Mix Oficial Gency
    "https://www.youtube.com/watch?v=LJSCBid9Szc", # Mix Geniales Live
    "https://www.youtube.com/watch?v=tfio0Un3fQs", # Mix Natusha
    "https://www.youtube.com/watch?v=OhsEGS6ZPQE"  # Technocumbias
]

# --- 3. FUNCIONES DE SOPORTE ---
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

# --- 4. LOGO "MADE IN PERÚ" ---
def crear_icono_rayo_peru():
    img = Image.new('RGB', (64, 64), color=(0, 0, 139))
    d = ImageDraw.Draw(img)
    # Rayo Dorado
    d.polygon([(40,5), (55,28), (38,28), (50,48), (14,35), (26,35)], fill=(255, 215, 0))
    # Sello
    try: fuente = ImageFont.truetype("arial.ttf", 10)
    except: fuente = ImageFont.load_default()
    d.text((2, 50), "MADE IN PERÚ", font=fuente, fill=(255, 215, 0))
    return img

def jalar_exito_aleatorio(icon=None, item=None):
    webbrowser.open(random.choice(PLAYLIST_GENRY))
    hablar("Cambiando el paso. Grupo Genry en el área.")

def iniciar_tray():
    try:
        menu = pystray.Menu(
            pystray.MenuItem("🎵 REPRODUCIR GRUPO GENRY", lambda i, n: jalar_exito_aleatorio()),
            pystray.MenuItem("⏭️ JALAR OTRO ÉXITO (Flecha)", jalar_exito_aleatorio),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("❌ CERRAR TANQUE", lambda i, n: i.stop())
        )
        icon = pystray.Icon("Genry", crear_icono_rayo_peru(), NOMBRE_APP, menu)
        icon.run()
    except: pass

# --- 5. ARRANQUE ---
if __name__ == "__main__":
    if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(NOMBRE_APP)
    threading.Thread(target=iniciar_tray, daemon=True).start()
    hablar(f"Sistema {FONETICA_NOMBRE} iniciado. Hardware identificado. Made in Perú.")
    while True: time.sleep(1)
