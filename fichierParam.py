
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

sleep(5)
x,y = pyautogui.locateCenterOnScreen("scot.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.doubleClick()

sleep(5)
x,y = pyautogui.locateCenterOnScreen("install.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.doubleClick()

sleep(3)
x,y = pyautogui.locateCenterOnScreen("size.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()
sleep(1)
pyautogui.click()

sleep(1)
x,y = pyautogui.locateCenterOnScreen("scoconfig.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("recevoir.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(5)
x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()