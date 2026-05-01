if __name__ == "__main__":
    # 1. Vinculamos con GitHub para descargar el CORE real[cite: 4]
    vincular_inteligencia_nube() 
    
    # 2. Lanzamos Guardián invisible para que vigile el tanque[cite: 1, 4]
    if os.name == 'nt' and os.path.exists("guardian.py"):
        subprocess.Popen([sys.executable, "guardian.py"], 
                         creationflags=subprocess.CREATE_NO_WINDOW)

    # 3. Iniciamos el motor de patrulla en segundo plano[cite: 4]
    motor = MotorGenryCentinela() 
    threading.Thread(target=motor.patrullar, daemon=True).start()
    
    # 4. Icono en la barra de tareas (Tray)[cite: 4]
    iniciar_tray()
