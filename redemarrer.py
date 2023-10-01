# import subprocess
# import platform

# def redemarrer_caisse(adresse_ip):
#     systeme_exploitation = platform.system()

#     if systeme_exploitation == "Windows":
#         # Commande pour redémarrer sur Windows en utilisant l'adresse IP
#         subprocess.run(["shutdown", "/m", adresse_ip, "/r", "/t", "0"], shell=True)

#     elif systeme_exploitation == "Linux" or systeme_exploitation == "Darwin":
#         # Commande pour redémarrer sur Linux ou macOS en utilisant l'adresse IP
#         commande_reboot = f"ssh {adresse_ip} sudo reboot"
#         subprocess.run(commande_reboot, shell=True)

#     else:
#         print("Redémarrage non pris en charge sur ce système d'exploitation.")

# # Adresse IP de la caisse à redémarrer
# adresse_ip_caisse = "10.37.99.14"

# # Appel de la fonction pour redémarrer la caisse spécifique
# redemarrer_caisse(adresse_ip_caisse)

# import subprocess

# def redemarrer_caisse(adresse_ip, username, password):
#     # Command to execute the Ansible playbook
#     command = f"ansible-playbook redemarrage_caisse.yml --extra-vars 'caisse_ip={adresse_ip} caisse_username={username} caisse_password={password}'"

#     try:
#         subprocess.run(command, shell=True)
#         print("Redémarrage de la caisse en cours...")
#     except Exception as e:
#         print(f"Erreur lors du redémarrage de la caisse : {str(e)}")

# # Adresse IP de la caisse à redémarrer
# adresse_ip_caisse = "128.129.189.43"

# # Nom d'utilisateur et mot de passe pour se connecter à la caisse
# caisse_username = "amal.riad"
# caisse_password = "Frozen@2001"

# # Appel de la fonction pour redémarrer la caisse
# redemarrer_caisse(adresse_ip_caisse, caisse_username, caisse_password)
import subprocess
import time
import pyautogui

# def redemarrer_caisse(adresse_ip, utilisateur, mot_de_passe):
#     # Étape 1: Connexion à distance à l'aide de UltraVNC ou du Bureau à distance
#     # Remplacez "chemin_vers_ultravnc" par le chemin vers l'exécutable UltraVNC ou "mstsc" pour le Bureau à distance
#     chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
#     subprocess.run([chemin_vers_ultravnc, adresse_ip])

#     # Attendez un certain temps pour permettre la connexion à distance de s'établir
#     time.sleep(2        
#                )
#     # Saisie automatique de l'utilisateur et du mot de passe dans la fenêtre UltraVNC
#     pyautogui.typewrite([utilisateur, '\t', mot_de_passe, '\t', '\n'])


    # Étape 2: Envoyer la commande de redémarrage de l'ordinateur
    # Remplacez "chemin_vers_shutdown" par le chemin vers l'exécutable de la commande d'arrêt à distance appropriée
    # chemin_vers_shutdown ="C:/Windows/System32/shutdown.exe"
    # subprocess.run([chemin_vers_shutdown, "/r", "/m", adresse_ip, "/u", utilisateur, "/p", mot_de_passe])

# # Adresse IP de la caisse à redémarrer
# adresse_ip_caisse = "10.38.98.153"

# # Nom d'utilisateur pour la connexion à distance
# utilisateur = "administrator"

# # Mot de passe pour la connexion à distance
# mot_de_passe = "Wind0ws10"

# # Appel de la fonction pour redémarrer la caisse
# redemarrer_caisse(adresse_ip_caisse, utilisateur, mot_de_passe)

# import subprocess
# import time
# import pyautogui

def redemarrer_caisse(adresse_ip, utilisateur, mot_de_passe):
    chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
    subprocess.Popen([chemin_vers_ultravnc, adresse_ip])

    # Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
    time.sleep(2)
    # Entrer le nom d'utilisateur et le mot de passe
    pyautogui.typewrite(utilisateur)
    pyautogui.press('tab')
    pyautogui.typewrite(mot_de_passe)
    pyautogui.press('enter')

#     # Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
#     time.sleep(2)
#     from pywinauto import Desktop

# # Se connecter à la caisse à distance en utilisant UltraVNC
# # Assurez-vous d'avoir déjà établi une connexion avec la caisse à distance

# # Recherchez la fenêtre principale d'UltraVNC
#     ultravnc_window = Desktop(backend="uia").window(class_name='ultravnc')

# # Cliquez sur le menu "Démarrer"
#     ultravnc_window.child_window(title="Démarrer").click_input()

# # Cliquez sur l'option "Redémarrer"
#     ultravnc_window.child_window(title="Redémarrer").click_input()  

# # Confirmez le redémarrage en cliquant sur le bouton "OK"
#     confirm_window = Desktop(backend="uia").window(title='Confirmer le redémarrage')
#     confirm_window.child_window(title='OK').click_input()


    # # Envoyer la combinaison de touches Ctrl + Échap pour afficher le menu UltraVNC
    # pyautogui.hotkey('ctrl', 'esc')

    # # Saisie automatique de l'utilisateur et du mot de passe dans la fenêtre UltraVNC
    # # pyautogui.typewrite([utilisateur, '\t', mot_de_passe, '\t', '\n'])

    # # Éventuellement, ajoutez un délai supplémentaire pour permettre la connexion à distance de s'établir
    # time.sleep(2)
    # # Redémarrer la caisse
    # pyautogui.hotkey('win', 'r')
    # pyautogui.typewrite('shutdown /r /t 0')
    # pyautogui.press('enter')

    # Étape 2: Envoyer la commande de redémarrage de l'ordinateur
    # chemin_vers_shutdown = "C:/Windows/System32/shutdown.exe"
    # subprocess.run([chemin_vers_shutdown, "/r", "/m", adresse_ip, "/u", utilisateur, "/p", mot_de_passe])
    # subprocess.run([chemin_vers_shutdown, "/r"])

# Adresse IP de la caisse à redémarrer
adresse_ip_caisse = "10.35.242.152"

# Nom d'utilisateur pour la connexion à distance
utilisateur = "administrator"

# Mot de passe pour la connexion à distance       

mot_de_passe = "Wind0ws10"

# Appel de la fonction pour redémarrer la caisse
redemarrer_caisse(adresse_ip_caisse, utilisateur, mot_de_passe)

# try:
#     while True:
#         x, y = pyautogui.position()
#         position_str = f"X: {x}, Y: {y}"
#         print(position_str, end="\r")
# except KeyboardInterrupt:
#     print("\nEnregistrement des coordonnées terminé.")