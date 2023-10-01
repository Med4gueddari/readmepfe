import subprocess
import xml.etree.ElementTree as ET
import pyautogui
import time 
from time import sleep
import pyperclip

# # ip_add="10.42.162.153"
# # # Ouvrir Bureau à distance
# # pyautogui.hotkey('win', 'r')
# # pyautogui.typewrite('mstsc')
# # pyautogui.press('enter')
# # time.sleep(2)
# #     # Entrer l'adresse IP
# # pyautogui.typewrite(ip_add)
# # pyautogui.press('enter')
# # time.sleep(5)

# # sleep(1)
# # x,y = pyautogui.locateCenterOnScreen("autre_choix.PNG",confidence=0.8)
# # pyautogui.moveTo(x, y, 1)
# # pyautogui.click()

# # sleep(1)
# # x,y = pyautogui.locateCenterOnScreen("autre_compte.PNG",confidence=0.9)
# # pyautogui.moveTo(x, y, 1)
# # pyautogui.click()

# # time.sleep(2)
# #     # Entrer le nom d'utilisateur et le mot de passe
# # utilisateur = "administrator"
# # pyautogui.typewrite(utilisateur)
# # pyautogui.press('tab')
# # mot_de_passe = "Wind0ws10"
# # pyautogui.typewrite(mot_de_passe)
# # pyautogui.press('enter')
# # time.sleep(2)
# #     # Envoyer la combinaison de touches Flèche gauche + Entrée pour effectuer une action dans UltraVNC
# # pyautogui.hotkey('left', 'enter')

# # sleep(10)
# # # Recherche du choix
# # choice = pyautogui.locateCenterOnScreen("bureau.PNG", confidence=0.9)
# # # Si le choix est trouvé, effectuer l'action
# # if choice is not None:
# #     x, y = choice
# #     pyautogui.moveTo(x, y, duration=1)
# #     pyautogui.click()
# #     pyautogui.click()
# # else:
# #     # Action "skip" lorsque le choix n'est pas trouvé
# #     print("Le choix n'a pas été trouvé. Skip...")

# # time.sleep(6)
# # # Recherche du premier choix
# # first_choice = pyautogui.locateCenterOnScreen("oui_but.PNG", confidence=0.7)

# # # Si le premier choix est trouvé, le sélectionner
# # if first_choice is not None:
# #     x, y = first_choice
# #     pyautogui.moveTo(x, y, duration=1)
# #     pyautogui.click()
# # else:
# #     # Recherche du deuxième choix
# #     second_choice = pyautogui.locateCenterOnScreen("oui_but2.PNG", confidence=0.7)
    
# #     # Si le deuxième choix est trouvé, le sélectionner
# #     if second_choice is not None:
# #         x, y = second_choice
# #         pyautogui.moveTo(x, y, duration=1)
# #         pyautogui.click()
# #     else:
# #         # Action "skip" lorsque aucun des choix n'est trouvé
# #         print("Aucun des choix n'a été trouvé. Skip...")

# # time.sleep(10)

# # # # Spécifiez la plage de temps à analyser (au format YYYY-MM-DDTHH:MM:SSZ)
# # deb_anomalie = '2023-05-23T10:00:00Z'
# # fin_anomalie = '2023-05-23T10:05:00Z'

# # # # Exécute la commande wevtutil pour obtenir les événements système au moment de l'anomalie
# # commande = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]"'

# # time.sleep(2)
# # pyautogui.typewrite('wevtutil qe System /q:"')
# # pyautogui.press('capslock')
# # sleep(0.5)
# # pyautogui.typewrite(':"')
# # pyautogui.press('capslock')

# # pyautogui.press('capslock')
# # pyautogui.typewrite('wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]"')

# # pyautogui.press("entrer")

# # sleep(5)
# # # Copier la sortie de la commande ipconfig
# # pyautogui.hotkey('ctrl', 'a')
# # command_output=pyautogui.hotkey('ctrl', 'c')
# # sleep(3)
# # # Fermer la fenêtre de commande
# # pyautogui.hotkey('alt', 'f4')

# # # resultat = subprocess.run(commande, capture_output=True, text=True)

# # with open('output.xml', 'w') as file:
# #     file.write(command_output)
# # # # Chemin et nom du fichier de sortie
# # # fichier_xml = 'resultat.xml'

# # # # Copie le résultat dans un fichier XML
# # # with open(fichier_xml, 'w') as f:
# # #     f.write(resultat.stdout)

# # Déterminer la plage horaire


# import datetime
# import subprocess
# import pyautogui
# import time

# # # Déterminer la plage horaire
# # now = datetime.datetime.now()
# # heure_precedente = now - datetime.timedelta(hours=1)

# # # Formater les horaires dans le format requis par la commande wevtutil
# # deb_anomalie = heure_precedente.strftime('%Y-%m-%dT%H:%M:%S')
# # fin_anomalie = now.strftime('%Y-%m-%dT%H:%M:%S')
deb_anomalie = '2023-05-23T10:00:00'
fin_anomalie = '2023-05-23T10:10:00'
# # Construire la commande wevtutil
# # command = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]"'

# # command1 = 'wevtutil qe System /q'
# # command2 =':"*'
# # command3='[System[TimeCreated['
# # command13='SystemTime>='
# # command7=f"{deb_anomalie}"
# # command9="00"
# # command10="] and TimeCreated["
# # command6='SystemTime'
# # command4 = '<'
# # command5 ='='
# # command12 =f"{fin_anomalie}"
# # command11=']]]'
# # command8 ='à'

# # # Ouvrir l'invite de commandes
# # pyautogui.hotkey('win', 'r')
# # pyautogui.typewrite('cmd')
# # pyautogui.press('enter')
# # time.sleep(2)

# # # Exécuter la commande wevtutil
# # pyautogui.typewrite(command1)
# # pyautogui.press('capslock')
# # pyautogui.typewrite(command2)
# # pyautogui.press('capslock')
# # pyautogui.typewrite(command3)
# # # Copy "@" symbol to clipboard
# # pyperclip.copy('@')

# # # Simulate Ctrl+V to paste "@" symbol
# # pyautogui.hotkey('ctrl', 'v')
# # pyautogui.typewrite(command13)
# # pyautogui.typewrite("'")
# # pyautogui.typewrite(command7)
# # pyautogui.press('capslock')
# # pyautogui.typewrite(':')
# # pyautogui.press('capslock')
# # pyautogui.typewrite(command9)
# # pyautogui.press('capslock')
# # pyautogui.typewrite(':')
# # pyautogui.press('capslock')
# # pyautogui.typewrite(command9)
# # pyautogui.press('capslock')
# # pyautogui.typewrite("z")
# # pyautogui.press('capslock')
# # pyautogui.typewrite("'")
# # pyautogui.typewrite(command10)
# # pyautogui.typewrite(['altgr'] + list(command8))
# # pyautogui.typewrite(command6)
# # pyautogui.typewrite(['shift'] + list(command4))
# # pyautogui.typewrite(command5)
# # pyautogui.typewrite("'")
# # pyautogui.typewrite(command12)
# # pyautogui.press('capslock')
# # pyautogui.typewrite(':')
# # pyautogui.press('capslock')
# # pyautogui.typewrite(command9)
# # pyautogui.press('capslock')
# # pyautogui.typewrite(':')
# # pyautogui.press('capslock')
# # pyautogui.typewrite(command9)
# # pyautogui.press('capslock')
# # pyautogui.typewrite("z")
# # pyautogui.press('capslock')
# # pyautogui.typewrite("'")
# # pyautogui.typewrite(command11)
# # pyautogui.press('capslock')
# # pyautogui.typewrite('"')
# # sleep(0.5)
# # pyautogui.press('enter')
# # command = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]" > "C:\\Users\\safouane.elharrak\\Documents\\Sujet PFE\\output.xml"'
# command = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]" > "Documents/output.xml"'

# cmd='wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>='2023-05-23T10:00:00Z'] and TimeCreated[@SystemTime>='2023-05-23T10:10:00Z']]]" > "Documents/output.xml"'
# Open the command prompt
# sleep(5)
# pyautogui.hotkey('win', 'r')
# pyautogui.typewrite('cmd')
# pyautogui.press('enter')
# time.sleep(2)

# # Execute the command and redirect the output to a file
# command = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime>=\'{fin_anomalie}\']]]" > "C:\Users\safouane.elharrak\Documents\Sujet PFE\output.xml"'
# pyperclip.copy(command)
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter')

# sleep(0.5)
# pyautogui.press('enter')

# # Attendre pour laisser le temps à la commande de s'exécuter
# # time.sleep(2)

# # # Copier la sortie de la commande
# # pyautogui.hotkey('ctrl', 'a')
# # pyautogui.hotkey('ctrl', 'c')

# # # Coller le contenu du presse-papiers dans un fichier .xml
# # command_output = pyperclip.paste()
# # if command_output is not None:
# #     with open('output.xml', 'w') as file:
# #         file.write(command_output)
# # else:
# #     print("La commande wevtutil n'a renvoyé aucune sortie.")


# # Ouvrir le dossier contenant le fichier à couper

sleep(5)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.typewrite('Documents')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Sélectionner le fichier à couper
sleep(5)
x,y = pyautogui.locateCenterOnScreen("outputimg.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()
time.sleep(1)
# pyautogui.press('down')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(1)

# Couper le fichier
pyautogui.hotkey('ctrl', 'x')
pyautogui.hotkey('ctrl', 'x')
time.sleep(1)

sleep(1)
x,y = pyautogui.locateCenterOnScreen("reduire.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
cmd ='Documents\Sujet PFE'
# Ouvrir le dossier de destination
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyperclip.copy(cmd)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(2)
x,y = pyautogui.locateCenterOnScreen("doc3.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()


# Coller le fichier
sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

sleep(1)
x,y = pyautogui.locateCenterOnScreen("bureau.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(1)
x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(1)
x,y = pyautogui.locateCenterOnScreen("ok.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()