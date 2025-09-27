#!/usr/bin/env python3

import psutil
import subprocess

def is_firefox_running():
    """Vérifie si Firefox est déjà en cours d'exécution."""
    for proc in psutil.process_iter(['name']):
        try:
            if 'firefox' in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def open_firefox():
    """Ouvre Firefox si ce n'est pas déjà en cours d'exécution."""
    if not is_firefox_running():
        print("Firefox n'est pas ouvert. Lancement de Firefox...")
        # Remplacez le chemin suivant par le chemin réel de votre exécutable Firefox
        subprocess.run(["firefox"])
    else:
        print("Firefox est déjà en cours d'exécution.")

if __name__ == "__main__":
    open_firefox()
