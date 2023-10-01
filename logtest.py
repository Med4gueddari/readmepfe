# import pyautogui
# import time
# from time import sleep
# import os
# import re

# pyautogui.hotkey('win', 'r')
# pyautogui.typewrite('mstsc')
# pyautogui.press('enter')
# time.sleep(2)
# ip_add ="10.42.162.154"
#     # Entrer l'adresse IP
# pyautogui.typewrite(ip_add)
# pyautogui.press('enter')
# time.sleep(5)

# sleep(1)
# x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()

# sleep(1)
# x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()

# time.sleep(2)
#     # Entrer le nom d'utilisateur et le mot de passe
# utilisateur = "administrator"
# pyautogui.typewrite(utilisateur)
# pyautogui.press('tab')
# mot_de_passe = "Wind0ws10"
# pyautogui.typewrite(mot_de_passe)
# pyautogui.press('enter')
# time.sleep(2)
#     # Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
# pyautogui.hotkey('left', 'enter')

# sleep(10)
# # Recherche du choix
# choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
# # Si le choix est trouvé, effectuer l'action
# if choice is not None:
#     x, y = choice
#     pyautogui.moveTo(x, y, duration=1)
#     pyautogui.click()
#     pyautogui.click()
# else:
#     # Action "skip" lorsque le choix n'est pas trouvé
#     print("Le choix n'a pas été trouvé. Skip...")

# time.sleep(6)
# # Recherche du premier choix
# first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

# # Si le premier choix est trouvé, le sélectionner
# if first_choice is not None:
#     x, y = first_choice
#     pyautogui.moveTo(x, y, duration=1)
#     pyautogui.click()
# else:
#     # Recherche du deuxième choix
#     second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
    
#     # Si le deuxième choix est trouvé, le sélectionner
#     if second_choice is not None:
#         x, y = second_choice
#         pyautogui.moveTo(x, y, duration=1)
#         pyautogui.click()
#     else:
#         # Action "skip" lorsque aucun des choix n'est trouvé
#         print("Aucun des choix n'a été trouvé. Skip...")

# # sleep(20)
# # x,y = pyautogui.locateCenterOnScreen("Ce_PC.PNG",confidence=0.9)
# # pyautogui.moveTo(x, y, 1)
# # pyautogui.click()


# log_directory = "C:\temp"

# logs = []
# for file_name in os.listdir(log_directory):
#     if re.match(r'^.*\.zip$', file_name, re.IGNORECASE):
#         logs.append(file_name)
# if not logs:
#     print("Aucun fichier log.zip trouvé dans le répertoire.")
# latest_log = max(logs)
# log_file = os.path.join(log_directory, latest_log)
# print(log_file)

# # sleep(5)
# # x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
# # pyautogui.moveTo(x, y, 1)
# # pyautogui.click()