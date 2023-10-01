
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

sleep(3)
# Coordonnées du modifié le
pyautogui.moveTo(1528, 147, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("grandir.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

time.sleep(2)
# Recherche du premier choix
fastlane_v1 = pyautogui.locateCenterOnScreen("fastlane_v1.PNG", confidence=0.7)
# Si le premier choix est trouvé, le sélectionner
if fastlane_v1 is not None:
    x, y = fastlane_v1
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    print("la version du fastlane est : 2.2.0.167.2")
else:
    # Recherche du deuxième choix
    fastlane_v2 = pyautogui.locateCenterOnScreen("fastlane_v2.PNG", confidence=0.7)
    # Si le deuxième choix est trouvé, le sélectionner
    if fastlane_v2 is not None:
        x, y = fastlane_v2
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    print("la version du fastlane est : 2.2.0.166.7")

    fastlane_v3 = pyautogui.locateCenterOnScreen("fastlane_v3.PNG", confidence=0.7)
    if fastlane_v3 is not None:
        x, y = fastlane_v3
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
        print("la version du fastlane est : 2.2.0.166.3")

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
