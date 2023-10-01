# import subprocess

# def get_qvs_version():
#     try:
#         # Exécute la commande "qvs --version" et capture la sortie
#         result = subprocess.run(['qvs', '--version'], capture_output=True, text=True)
#         output = result.stdout.strip()
        
#         # Extrait la version à partir de la sortie
#         version = output.split()[-1]
#         return version
#     except FileNotFoundError:
#         return "QVS n'est pas installé."

# def get_fastlane_version():
#     try:
#         # Exécute la commande "fastlane --version" et capture la sortie
#         result = subprocess.run(['fastlane', '--version'], capture_output=True, text=True)
#         output = result.stdout.strip()
        
#         # Extrait la version à partir de la sortie
#         version = output.split()[-1]
#         return version
#     except FileNotFoundError:
#         return "Fastlane n'est pas installé."

# # Vérifie la version de QVS
# qvs_version = get_qvs_version()
# print("Version de QVS :", qvs_version)

# # Vérifie la version de Fastlane
# fastlane_version = get_fastlane_version()
# print("Version de Fastlane :", fastlane_version)


import subprocess
import time
from time import sleep
import pyautogui

ip_add="10.36.18.167"
chemin_vers_ultravnc = "C:/Users/safouane.elharrak/Documents/ULTRAVNC/ULTRAVNC/vncviewer.exe"
subprocess.Popen([chemin_vers_ultravnc, ip_add])
# Attendez un certain temps pour permettre la fenêtre UltraVNC de s'afficher
sleep(1)
# Nom d'utilisateur pour la connexion à distance
utilisateur = "administrator"
# Mot de passe pour la connexion à distance       
mot_de_passe = "Wind0ws10"
time.sleep(2)
# Entrer le nom d'utilisateur et le mot de passe
pyautogui.typewrite(utilisateur)
pyautogui.press('tab')
pyautogui.typewrite(mot_de_passe)
pyautogui.press('enter')

sleep(5)
x,y = pyautogui.locateCenterOnScreen("fichier.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("my_doc.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.doubleClick()

sleep(25)
x,y = pyautogui.locateCenterOnScreen("disk_C.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.doubleClick()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("install.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.doubleClick()

# sleep(3)
# # Coordonnées du modifié le
# pyautogui.moveTo(1528, 147, 1)
# pyautogui.click()

time.sleep(2)
# Recherche du premier choix
qvs_v1 = pyautogui.locateCenterOnScreen("qvsv1.PNG", confidence=0.7)
# Si le premier choix est trouvé, le sélectionner
if qvs_v1 is not None:
    x, y = qvs_v1
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    print("QVS version est : 8.10.11.0")
else:
    # Recherche du deuxième choix
    qvs_v2 = pyautogui.locateCenterOnScreen("qvsv2.PNG", confidence=0.7)
    # Si le deuxième choix est trouvé, le sélectionner
    if qvs_v2 is not None:
        x, y = qvs_v2
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
        print("QVS version est : 7.7.12.0")

    else:
        # Action "skip" lorsque aucun des choix n'est trouvé
        print("Probleme de trouvé la version")

sleep(2)
x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()
