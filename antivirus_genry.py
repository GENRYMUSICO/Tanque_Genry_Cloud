# --- CONECTOR DE INTELIGENCIA MODULAR ---

def cargar_core_desde_nube():
    """Descarga e inyecta las funciones críticas consolidadas"""
    try:
        # URL Raw de su nuevo archivo CORE_SISTEMA.txt
        url = f"https://raw.githubusercontent.com/{USUARIO_GH}/{REPO_GH}/main/CORE_SISTEMA.txt"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            # Ejecuta el código descargado para definir las funciones al vuelo
            exec(r.text, globals())
            print("[SISTEMA] CORE cargado con éxito. ADN, Voz y Hashes activos.")
        else:
            print("[ERROR] No se pudo conectar con el CORE en la nube.")
    except Exception as e:
        print(f"[CRÍTICO] Fallo en la inyección de inteligencia: {e}")

# --- EN EL ARRANQUE DEL TANQUE ---

if __name__ == "__main__":
    descargar_recursos_nube() # Logos y bases
    cargar_core_desde_nube()    # Inyección de las funciones del CORE[cite: 8]
    
    # Ahora ya puede usar 'hablar' o 'obtener_adn_maquina' aunque no estén escritas aquí[cite: 8]
    verificar_expiracion_y_limpiar()
    
    motor = MotorGenryCentinela()
    threading.Thread(target=motor.patrullar, daemon=True).start()
    
    hablar(f"Sistema {FONETICA_NOMBRE} V 1 punto 8 75. Inteligencia modular activada.")
    iniciar_tray()
