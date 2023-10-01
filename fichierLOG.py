# import os
# import re

# def enumerate_errors(log_directory, error_keywords):
#     logs = []
#     for file_name in os.listdir(log_directory):
#         if re.match(r'^.*\.zip$', file_name, re.IGNORECASE):
#             logs.append(file_name)
#     if not logs:
#         print("Aucun fichier log.zip trouvé dans le répertoire.")
#         return []

#     latest_log = max(logs)
#     log_file = os.path.join(log_directory, latest_log)
#     print(log_file)
#     return extract_errors_from_zip(log_file, error_keywords)

# def extract_errors_from_zip(log_file, error_keywords):
#     errors = []
#     # Code pour extraire les fichiers log du zip et les analyser
#     # Adaptation nécessaire selon le format du log.zip et les outils utilisés
#     # Vous pouvez utiliser la bibliothèque zipfile pour extraire les fichiers log.zip

#     return errors

# # Exemple d'utilisation
# log_directory = "C:/Users/safouane.elharrak/Desktop/Test"
# error_keywords = ["erreur", "problème", "exception"]

# error_lines = enumerate_errors(log_directory, error_keywords)
# for line in error_lines:
#     print(line)

# # import paramiko

# # def copy_file_from_remote(remote_host, remote_username, remote_password, remote_file_path, local_file_path):
# #     ssh = paramiko.SSHClient()
# #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #     ssh.connect(remote_host, username=remote_username, password=remote_password)

# #     sftp = ssh.open_sftp()
# #     sftp.get(remote_file_path, local_file_path)

# #     sftp.close()
# #     ssh.close()

# # # Exemple d'utilisation
# # remote_host = '10.34.82.154'
# # remote_username = 'administrator'
# # remote_password = 'Wind0ws10'
# # remote_file_path = 'C:\temp\FRHY0001CLSS05-230523-130001.zip\FRHY0001CLSS05-230523-130001.7z'
# # local_file_path = 'C:/Users/safouane.elharrak/Deskto/Test'

# # copy_file_from_remote(remote_host, remote_username, remote_password, remote_file_path, local_file_path)


import subprocess
import time
from time import sleep
import pyautogui

ip_add="10.34.82.152"
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
x,y = pyautogui.locateCenterOnScreen("temp.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.doubleClick()

sleep(3)
# trier_modified = (1528, 147)  # Coordonnées du champ de saisie pour l'adresse IP ou le nom d'hôte
pyautogui.moveTo(1528, 147, 1)
pyautogui.click()
# x,y = pyautogui.locateCenterOnScreen("size.PNG",confidence=0.8)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()
# x,y = pyautogui.locateCenterOnScreen("modified.PNG",confidence=0.8)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()
# pyautogui.hotkey('down')

# try:
#     while True:
#         x, y = pyautogui.position()
#         position_str = f"X: {x}, Y: {y}"
#         print(position_str, end="\r")
# except KeyboardInterrupt:
#     print("\nEnregistrement des coordonnées terminé.")

sleep(2)
x,y = pyautogui.locateCenterOnScreen("FRHY2.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("recevoir.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(20)
x,y = pyautogui.locateCenterOnScreen("sortir.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()

sleep(2)
x,y = pyautogui.locateCenterOnScreen("sortir2.PNG",confidence=0.8)
pyautogui.moveTo(x, y, 1)
pyautogui.click()