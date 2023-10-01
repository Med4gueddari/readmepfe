import pyautogui
import time
import subprocess

from WithMysql import get_ip

# Appeler la fonction et obtenir la valeur retournée
# resultat = get_ip()

# Utiliser la valeur retournée
# print(resultat)  # Affiche : 42

# Désactiver le comportement de sécurité de PyAutoGUI pour bloquer le curseur
# pyautogui.FAILSAFE = False

# Attendre quelques secondes pour laisser le temps de basculer vers la fenêtre UltraVNC
time.sleep(5)

# Coordonnées initiales du curseur
# initial_position = pyautogui.position()

# Réserver le curseur en maintenant le bouton de la souris enfoncé
pyautogui.mouseDown()


# Chemin d'accès à l'exécutable UltraVNC (à adapter selon votre installation)
ultravnc_path = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"

# Lancer UltraVNC
subprocess.Popen(ultravnc_path)
# Attendre quelques secondes pour laisser le temps de basculer vers la fenêtre UltraVNC
time.sleep(2)

# Coordonnées des boutons et champs de saisie dans l'interface UltraVNC (à adapter selon votre configuration)
host_input = (1140, 297)  # Coordonnées du champ de saisie pour l'adresse IP ou le nom d'hôte
connect_button = (1159, 363)  # Coordonnées du bouton "Connect" ou "Connexion"
plugin_button = (720, 617)  # Coordonnées du bouton "DSMplugin"

username_input = (1010, 480)  # Coordonnées du champ de saisie pour le nom d'utilisateur
password_input = (1004, 520)  # Coordonnées du champ de saisie pour le mot de passe

connexion_button = (1005, 567)  # Coordonnées du bouton "Connect" ou "Connexion"


# Entrer l'adresse IP ou le nom d'hôte de la machine distante
pyautogui.click(host_input)

# Effectuer une combinaison de touches pour vider le champ de saisie
pyautogui.hotkey('ctrl', 'a')  # Sélectionner tout le texte
pyautogui.press('delete')  # Supprimer le texte sélectionné
pyautogui.typewrite('10.36.18.150')  # Remplacez par l'adresse IP ou le nom d'hôte réel

# # Cliquer sur le bouton "DSMplugin" 
# pyautogui.click(plugin_button)

# # Attendre quelques secondes pour laisser le temps de basculer 
# time.sleep(2)

# # Cliquer sur le bouton "Connect" ou "Connexion"
# pyautogui.click(connect_button)

# # Attendre quelques secondes pour laisser le temps de basculer 
# time.sleep(3)

# # Entrer le nom d'utilisateur
# pyautogui.click(username_input)
# pyautogui.typewrite('administrator')  

# # Entrer le mot de passe
# pyautogui.click(password_input)
# pyautogui.typewrite('Wind0ws10')  

# # Attendre quelques secondes pour laisser le temps de basculer 
# time.sleep(1)

# # Cliquer sur le bouton "Connexion"
# pyautogui.click(connexion_button)

# Relâcher le bouton de la souris pour libérer le curseur
pyautogui.mouseUp()



###################################################################################

# print("Déplacez le curseur de la souris sur les éléments d'interface UltraVNC...")
# print("Appuyez sur Ctrl+C pour arrêter l'enregistrement des coordonnées.\n")

# try:
#     while True:
#         x, y = pyautogui.position()
#         position_str = f"X: {x}, Y: {y}"
#         print(position_str, end="\r")
# except KeyboardInterrupt:
#     print("\nEnregistrement des coordonnées terminé.")


