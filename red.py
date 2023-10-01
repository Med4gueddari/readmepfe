import pyautogui
import time

def redemarrer_caisse(ip, utilisateur, mot_de_passe):
    # Ouvrir UltraVNC ou Bureau à distance
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('mstsc')
    pyautogui.press('enter')
    time.sleep(2)

    # Entrer l'adresse IP
    pyautogui.typewrite(ip)
    pyautogui.press('enter')
    time.sleep(5)
    autre_choix = (705, 490)  # Coordonnées du bouton "Connect" ou "Connexion"
    pyautogui.click(autre_choix)
    time.sleep(2)
    autre_utilisateur = (840, 650)  # Coordonnées du bouton "DSMplugin"
    pyautogui.click(autre_utilisateur)
    time.sleep(2)
    # Entrer le nom d'utilisateur et le mot de passe
    pyautogui.typewrite(utilisateur)
    pyautogui.press('tab')
    pyautogui.typewrite(mot_de_passe)
    pyautogui.press('enter')
    time.sleep(2)
    # Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
    pyautogui.hotkey('left', 'enter')
    time.sleep(6)

    oui_button = (878, 741)  # Coordonnées du bouton "DSMplugin"
    pyautogui.click(oui_button)
    pyautogui.click(oui_button)
    time.sleep(10)


    # Redémarrer la caisse
    # pyautogui.hotkey('win', 'r')
    # pyautogui.typewrite('shutdown /r /t 0')
    # pyautogui.press('enter')
    # time.sleep(2)

    # # Fermer la session à distance
    # pyautogui.hotkey('alt', 'f4')
    # pyautogui.press('enter')

# Exemple d'utilisation
# Adresse IP de la caisse à redémarrer
adresse_ip = "10.35.242.157"

# Nom d'utilisateur pour la connexion à distance
utilisateur = "administrator"

# Mot de passe pour la connexion à distance
mot_de_passe = "Wind0ws10"

redemarrer_caisse(adresse_ip, utilisateur, mot_de_passe)

# from pywinauto import Application

# def cliquer_sur_bouton(mot_cle):
#     # Chemin vers le fichier exécutable du logiciel
#     chemin_vers_logiciel = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"

#     # Créer une instance de l'application
#     application = Application().start(chemin_vers_logiciel)

#     # Attente pour permettre le lancement complet de l'application
#     application.wait_cpu_usage_lower(threshold=5, timeout=10)

#     # Sélectionner la fenêtre principale de l'application
#     fenetre_principale = application.window()

#     # Trouver le bouton correspondant au mot-clé
#     bouton = fenetre_principale.window(title_re=f".*{mot_cle}.*", control_type="Button")

#     # Cliquer sur le bouton
#     bouton.click()

#     # Fermer l'application
#     application.kill()

# # Exemple d'utilisation : cliquer sur le bouton "Autre choix" dans le logiciel
# mot_cle_bouton = "Connecter"
# cliquer_sur_bouton(mot_cle_bouton)

# import paramiko

# def reboot_remote_machine(ip_address, username, password):
#     # Établir une connexion SSH
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(ip_address, username=username, password=password)

#     # Exécuter la commande de redémarrage
#     ssh.exec_command('shutdown /r /t 0')

#     # Fermer la connexion SSH
#     ssh.close()

# # Exemple d'utilisation
# ip_address = '10.35.242.156'  # Adresse IP de la machine distante
# username = 'administrator'            # Nom d'utilisateur administrateur
# password = 'Wind0ws10'         # Mot de passe administrateur

# reboot_remote_machine(ip_address, username, password)
