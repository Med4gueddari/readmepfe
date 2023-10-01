# import socket

# def test_connexion(adresse_ip):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex((adresse_ip, 80))
#     if result == 0:
#         print(f"La connexion vers {adresse_ip} est réussie.")
#     else:
#         print(f"La connexion vers {adresse_ip} a échoué.")

# # Exemple d'utilisation pour tester une seule adresse IP
# adresse_ip = "10.45.114.152"  # Remplacez par l'adresse IP de la caisse ou du magasin
# test_connexion(adresse_ip)


from ping3 import ping, verbose_ping

def test_ping(adresse_ip):
    response_time = ping(adresse_ip)
    if response_time is not None:
        print(f"Le ping vers {adresse_ip} a réussi. Temps de réponse : {response_time} ms")
    else:
        print(f"Le ping vers {adresse_ip} a échoué.")

# def test_ping(adresse_ip):
#     result = verbose_ping(adresse_ip, count=4, timeout=2)
#     if result:
#         print(f"Le ping vers {adresse_ip} a réussi.")
#     else:
#         print(f"Le ping vers {adresse_ip} a échoué.")

# Exemple d'utilisation pour tester une seule adresse IP
adresse_ip = "10.45.114.152"  # Remplacez par l'adresse IP de la caisse ou du magasin
test_ping(adresse_ip)
