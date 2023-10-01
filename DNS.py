import subprocess
import os
# def get_dns_servers():
#     dns_servers = []
    
#     try:
#         # Exécute la commande "ipconfig /all" (sur Windows) ou "cat /etc/resolv.conf" (sur macOS/Linux) et capture la sortie
#         if os.name == 'nt':  # Windows
#             result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
#             output = result.stdout.strip()
#         # else:  # macOS/Linux
#         #     result = subprocess.run(['cat', '/etc/resolv.conf'], capture_output=True, text=True)
#         #     output = result.stdout.strip()
        
#         # Analyse la sortie pour extraire les serveurs DNS
#         lines = output.split('\n')
#         for line in lines:
#             if 'Serveurs DNS' in line:
#                 dns_servers_line = line.split(':')
#                 if len(dns_servers_line) > 1:
#                     servers = dns_servers_line[1].strip().split(' ')
#                     dns_servers.extend(servers)
        
#     except FileNotFoundError:
#         print("Impossible de récupérer les paramètres DNS.")
    
#     return dns_servers

# def compare_dns_servers():
#     # Récupère les paramètres DNS
#     dns_servers = get_dns_servers()
    
#     if len(dns_servers) < 2:
#         print("Il n'y a pas suffisamment de serveurs DNS pour comparer.")
#         return
    
#     # Vérifie si tous les serveurs DNS sont identiques
#     if all(server == dns_servers[0] for server in dns_servers):
#         print("Tous les serveurs DNS sont identiques :", dns_servers[0])
#     else:
#         print("Les serveurs DNS sont différents :", dns_servers)

# # Appel de la fonction pour comparer les paramètres DNS
# compare_dns_servers()





import pyautogui
import time
from time import sleep
import clipboard
import re


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

# Attendre que la connexion soit établie et les paramètres DNS s'affichent
time.sleep(5)

# Récupérer les paramètres DNS
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('cmd')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('ipconfig')
pyautogui.press('capslock')
pyautogui.typewrite('/all')

pyautogui.press('enter')
time.sleep(2)

# Copier la sortie de la commande ipconfig
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
sleep(1)
# Fermer la fenêtre de commande
pyautogui.hotkey('alt', 'f4')

# Comparer les paramètres DNS
dns_output = clipboard.paste()
dns_lines = dns_output.split('\n')
for line in dns_lines:
    if "Serveurs DNS" in line:
        dns_servers = line.split(':')[1].strip()
        if dns_servers == "Serveurs DNS attendus ": #Expected DNS Servers
            print("Les paramètres DNS sont corrects.")
        else:
            print("Les paramètres DNS ne correspondent pas.")
# dns_servers=[]
# lines = dns_output.split('\n')
# print(lines)
# try:
#     for line in lines:
#         if 'Serveurs DNS' in line:
#             dns_servers_line = line.split(':')
#             if len(dns_servers_line) > 1:
#                 servers = dns_servers_line[1].strip().split(' ')
#                 # ip_addresses = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
#                 dns_servers.extend(servers)
#                 print(dns_servers)
# except FileNotFoundError:
#     print("Impossible de récupérer les paramètres DNS.")

# if len(dns_servers) < 2:
#     print("Il n'y a pas suffisamment de serveurs DNS pour comparer.")
    
# # Vérifie si tous les serveurs DNS sont identiques
# if all(server == dns_servers[0] for server in dns_servers):
#     print("Tous les serveurs DNS sont identiques :", dns_servers[0])
# else:
#     print("Les serveurs DNS sont différents :", dns_servers)
dns_servers=[]
found_dns_servers = False
next_lines_count = 3
lines = dns_output.split('\n')
print(lines)
try:
    for line in lines:
        if 'Serveurs DNS' in line:
            found_dns_servers = True
            dns_servers.extend(line.split(':')[1].strip().split())

        elif found_dns_servers and next_lines_count > 0:
            dns_servers.append(line.strip())
            next_lines_count -= 1
            dns_servers_line = line.split(':')
            if len(dns_servers_line) > 1:
                servers = dns_servers_line[1].strip().split(' ')
                # ip_addresses = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
                dns_servers.extend(servers)
                print(dns_servers)
except FileNotFoundError:
    print("Impossible de récupérer les paramètres DNS.")

if len(dns_servers) < 2:
    print("Il n'y a pas suffisamment de serveurs DNS pour comparer.")
    
# Vérifie si tous les serveurs DNS sont identiques
if all(server == dns_servers[0] for server in dns_servers):
    print("Tous les serveurs DNS sont identiques :", dns_servers[0])
else:
    print("Les serveurs DNS sont différents :", dns_servers)

# # Fermer la session Bureau à distance
# pyautogui.hotkey('alt', 'f4')
# pyautogui.hotkey('alt', 'f4')

# liste = [
#     'Microsoft Windows [version 10.0.14393]\r',
#     '(c) 2016 Microsoft Corporation. Tous droits réservés.\r',
#     '\r',
#     'C:\\Users\\Administrator>ipconfig/ALL\r',
#     '\r',
#     'Configuration IP de Windows\r',
#     '\r',
#     '   Nom de l’hôte . . . . . . . . . . : FRHY0508CLSS03\r',
#     '   Suffixe DNS principal . . . . . . : dg.carrefour.com\r',
#     '   Type de noeud. . . . . . . . . .  : Hybride\r',
#     '   Routage IP activé . . . . . . . . : Non\r',
#     '   Proxy WINS activé . . . . . . . . : Non\r',
#     '   Liste de recherche du suffixe DNS.: dg.carrefour.com\r',
#     '           ho.fr.wcorp.carrefour.com\r',
#     '                                       carrefour.com\r',
#     '\r',
#     'Carte Ethernet Ethernet :\r',
#     '\r',
#     '   Suffixe DNS propre à la connexion. . . :\r',
#     '   Description. . . . . . . . . . . . . . : Intel(R) Ethernet Connection I217-LM\r',
#     '   Adresse physique . . . . . . . . . . . : 3C-E1-A1-3C-AE-77\r',
#     '   DHCP activé. . . . . . . . . . . . . . : Non\r',
#     '   Configuration automatique activée. . . : Oui\r',
#     '   Adresse IPv6 de liaison locale. . . . .: fe80::fd88:cf19:2bcb:a88%4(préféré)\r',
#     '   Adresse IPv4. . . . . . . . . . . . . .: 10.35.242.152(préféré)\r',
#     '   Masque de sous-réseau. . . .\xa0. . . . . : 255.255.254.0\r',
#     '   Passerelle par défaut. . . .\xa0. . . . . : 10.35.243.254\r',
#     '   IAID DHCPv6 . . . . . . . . . . . : 54321569\r',
#     '   DUID de client DHCPv6. . . . . . . . : 00-01-00-01-25-F1-23-77-3C-E1-A1-3C-AE-77\r',
#     '   Serveurs DNS. . .  . . . . . . . . . . : 10.48.241.1\r',
#     '         10.54.76.1\r',
#     '                                       10.48.241.2\r',
#     '                                       10.48.241.3\r',
#     '\r',
#     'Adresse physique . . . . . . . . . . . : 00-00-00-00-00-00-00-E0\r',
#     '   DHCP activé. . . . . . . . . . . . . . : Non\r',
#     '   Configuration automatique activée. . . : Oui\r',
#     '\r',
#     'C:\\Users\\Administrator>'
# ]

# # dns_servers = []
# # found_dns_servers = False
# # next_lines_count = 3

# # for line in liste:
# #     if 'Serveurs DNS' in line:
# #         found_dns_servers = True
# #         dns_servers.extend(line.split(':')[1].strip().split())

# #     elif found_dns_servers and next_lines_count > 0:
# #         dns_servers.append(line.strip())
# #         next_lines_count -= 1

# # print(dns_servers)

# # dns_output = liste


# # dns_lines = dns_output.split('\n')
# # for line in dns_lines:
# #     if "Serveurs DNS" in line:
# #         dns_servers = line.split(':')[1].strip()
# #         if dns_servers == "Serveurs DNS attendus ": #Expected DNS Servers
# #             print("Les paramètres DNS sont corrects.")
# #         else:
# #             print("Les paramètres DNS ne correspondent pas.")
            
# dns_servers=[]
# found_dns_servers = False
# next_lines_count = 3
# lines = dns_output
# try:
#     for line in lines:
#         if 'Serveurs DNS' in line:
#             found_dns_servers = True
#             dns_servers.extend(line.split(':')[1].strip().split())

#         elif found_dns_servers and next_lines_count > 0:
#             dns_servers.append(line.strip())
#             next_lines_count -= 1
#             dns_servers_line = line.split(':')
#             if len(dns_servers_line) > 1:
#                 servers = dns_servers_line[1].strip().split(' ')
#                 # ip_addresses = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
#                 dns_servers.extend(servers)
#                 print(dns_servers)
# except FileNotFoundError:
#     print("Impossible de récupérer les paramètres DNS.")

# if len(dns_servers) < 2:
#     print("Il n'y a pas suffisamment de serveurs DNS pour comparer.")
    
# # Vérifie si tous les serveurs DNS sont identiques
# if all(server == dns_servers[0] for server in dns_servers):
#     print("Tous les serveurs DNS sont identiques :", dns_servers[0])
# else:
#     print("Les serveurs DNS sont différents :", dns_servers)
