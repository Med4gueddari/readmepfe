# import pyautogui
# from time import sleep
# #locate the image on screen
# res = pyautogui.locateAllOnScreen("")
# print(res)
# #get the center coordinates of the image
# edit_butt=pyautogui.center(res)

# #locate the center of the image on the screen
# res=pyautogui.locateCenterOnScreen("")
# print(res)

# #popup to take input
# channel_name = pyautogui.prompt(text="",title="Entrer the Channel Name")
# print(channel_name)
# #opens new tab
# pyautogui.hotkey("ctrl","t")
# sleep(1)
# #search youtube
# pyautogui.write("http://www.youtube.com/")
# pyautogui.hotkey("entrer")

# sleep(1)
# x,y = pyautogui.locateCenterOnScreen("",confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()

# sleep(1)
# #search the channel name
# pyautogui.write(channel_name)
# pyautogui.hotkey("entrer")

# sleep(1)
# x,y = pyautogui.locateCenterOnScreen("",confidence=0.8)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()

# sleep(1)
# x,y = pyautogui.locateCenterOnScreen("",confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()

import pyautogui
import time
from time import sleep

    # Ouvrir UltraVNC ou Bureau à distance
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('mstsc')
pyautogui.press('enter')
time.sleep(2)

ip = "10.35.242.152"
    # Entrer l'adresse IP
pyautogui.typewrite(ip)
pyautogui.press('enter')
time.sleep(5)

sleep(1)
x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(1)
x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

time.sleep(2)
    # Entrer le nom d'utilisateur et le mot de passe
utilisateur = "administrator"
pyautogui.typewrite(utilisateur)
pyautogui.press('tab')
mot_de_passe = "Wind0ws10"
pyautogui.typewrite(mot_de_passe)
pyautogui.press('enter')
time.sleep(2)
    # Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
pyautogui.hotkey('left', 'enter')

sleep(10)
# Recherche du choix
choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
# Si le choix est trouvé, effectuer l'action
if choice is not None:
    x, y = choice
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    pyautogui.click()
else:
    # Action "skip" lorsque le choix n'est pas trouvé
    print("Le choix n'a pas été trouvé. Skip...")
    # Ajoutez ici le code pour effectuer l'action de "skip" souhaitée
    # Si vous ne souhaitez rien faire dans ce cas, laissez simplement ce bloc vide


time.sleep(6)
# Recherche du premier choix
first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

# Si le premier choix est trouvé, le sélectionner
if first_choice is not None:
    x, y = first_choice
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
else:
    # Recherche du deuxième choix
    second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
    
    # Si le deuxième choix est trouvé, le sélectionner
    if second_choice is not None:
        x, y = second_choice
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.click()
    else:
        # Action "skip" lorsque aucun des choix n'est trouvé
        print("Aucun des choix n'a été trouvé. Skip...")
        # Ajoutez ici le code pour effectuer l'action de "skip" souhaitée


# time.sleep(10)
#     # Redémarrer la caisse
# pyautogui.hotkey('win', 'r')
# sleep(2)
# # pyautogui.typewrite('shutdown /r /t 0 ')
# pyautogui.typewrite('shutdown')
# pyautogui.press('capslock')
# pyautogui.typewrite(' /r /t 0')
# sleep(1)
# pyautogui.press('enter')
# time.sleep(2)