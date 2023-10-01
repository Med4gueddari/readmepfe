# import win32evtlog
# import datetime

# def analyser_evenements_systeme(debut, fin):
#     log_type = 'System'  # Type de journal des événements système
#     server = None  # Laissez cette valeur à None pour accéder aux événements locaux

#     debut_dt = datetime.datetime.strptime(debut, '%Y-%m-%d %H:%M:%S')
#     fin_dt = datetime.datetime.strptime(fin, '%Y-%m-%d %H:%M:%S')

#     hand = win32evtlog.OpenEventLog(server, log_type)
#     flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

#     events = []
#     while True:
#         events_buffer = win32evtlog.ReadEventLog(hand, flags, 0)
#         if events_buffer:
#             for event in events_buffer:
#                 event_time = event.TimeGenerated
#                 if debut_dt <= event_time <= fin_dt:
#                     events.append(event)
#         else:
#             break

#     win32evtlog.CloseEventLog(hand)

#     return events

# # Spécifiez la plage de temps à analyser (au format YYYY-MM-DD HH:MM:SS)
# debut_anomalie = '2023-05-23 10:00:00'
# fin_anomalie = '2023-05-23 13:00:00'

# evenements = analyser_evenements_systeme(debut_anomalie, fin_anomalie)

# for evenement in evenements:
#     print(f"Date/heure : {evenement.TimeGenerated}")
#     print(f"Source : {evenement.SourceName}")
#     print(f"Description : {evenement.StringInserts}")
#     print("----------------------")
# # import win32evtlog

# # def get_system_events(log_type='System', event_type='error'):
# #     event_log = win32evtlog.OpenEventLog(None, log_type)
# #     events = []
    
# #     flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
# #     total_records = win32evtlog.GetNumberOfEventLogRecords(event_log)
    
# #     while True:
# #         events_batch = win32evtlog.ReadEventLog(event_log, flags, 0)
# #         if not events_batch:
# #             break
        
# #         for event in events_batch:
# #             if event.EventType == win32evtlog.EVENTLOG_ERROR_TYPE:
# #                 events.append({
# #                     'EventID': event.EventID,
# #                     'TimeGenerated': event.TimeGenerated.Format(),
# #                     'SourceName': event.SourceName,
# #                     'EventCategory': event.EventCategory,
# #                     'Description': event.StringInserts
# #                 })
    
# #     win32evtlog.CloseEventLog(event_log)
# #     return events

# # # Exemple d'utilisation
# # events = get_system_events(log_type='System', event_type='error')

# # for event in events:
# #     print('Event ID:', event['EventID'])
# #     print('Time Generated:', event['TimeGenerated'])
# #     print('Source Name:', event['SourceName'])
# #     print('Event Category:', event['EventCategory'])
# #     print('Description:', event['Description'])
# #     print('---')


# import subprocess
# import xml.etree.ElementTree as ET


# # # Spécifiez la plage de temps à analyser (au format YYYY-MM-DDTHH:MM:SSZ)
# deb_anomalie = '2023-05-23T10:00:00Z'
# fin_anomalie = '2023-05-23T11:00:00Z'

# # # Exécute la commande wevtutil pour obtenir les événements système au moment de l'anomalie
# commande = f'wevtutil qe System /q:"*[System[TimeCreated[@SystemTime>=\'{deb_anomalie}\'] and TimeCreated[@SystemTime<=\'{fin_anomalie}\']]]"'
# resultat = subprocess.run(commande, capture_output=True, text=True)

# # Chemin et nom du fichier de sortie
# fichier_xml = 'resultat.xml'

# # Copie le résultat dans un fichier XML
# with open(fichier_xml, 'w') as f:
#     f.write(resultat.stdout)

# # # Copie le résultat dans un fichier XML
# # with open(fichier_xml, 'w') as f:
# #     f.write(resultat.stdou
# # Lit le contenu du fichier XML
# with open(fichier_xml, 'r') as f:
#     xml_string = f.read()
# # Analyse le fichier XML et extrait les informations des événements système
# # tree = ET.parse(fichier_xml)
# # root = tree.getroot()

# # for event in root.findall('.//Event'):
# #     time_created = event.find('.//TimeCreated').attrib['SystemTime']
# #     source_name = event.find('.//Provider').attrib['Name']
# #     description = event.find('.//Message').text

# #     print(f"Date/heure : {time_created}")
# #     print(f"Source : {source_name}")
# #     print(f"Description : {description}")
# #     print("----------------------")
# root = ET.fromstring(xml_string)
# print(root)
# # for event in root.findall('.//Event'):
# #     time_created = event.find('.//TimeCreated').attrib['SystemTime']
# #     source_name = event.find('.//Provider').attrib['Name']
# #     description = event.find('.//Message').text

# #     print(f"Date/heure : {time_created}")
# #     print(f"Source : {source_name}")
# #     print(f"Description : {description}")
# #     print("----------------------")


# import xml.etree.ElementTree as ET

# # Chemin vers le fichier XML
# # xml_file = "resultat.xml"
# xml_string ="resultat.xml"

# # Parsing du fichier XML
# # tree = ET.parse(xml_file)
# # print(tree)
# # root = tree.getroot()
# root = ET.fromstring(open('resultat.xml').read())


# print(root)

# for event in root.findall('.//Event'):
#     time_created = event.find('.//TimeCreated').attrib['SystemTime']
#     source_name = event.find('.//Provider').attrib['Name']
#     description = event.find('.//Message').text
#     print(f"Date/heure : {time_created}")
#     print(f"Source : {source_name}")
#     print(f"Description : {description}")
#     print("----------------------")

# import subprocess

# def run_command(command):
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, error = process.communicate()
#     return output.decode(), error.decode()

# # Liste des commandes à exécuter
# commands = [
#     'wevtutil qe System /q:"*[System[TimeCreated[timediff(@SystemTime) <= 86400000]]]" /rd:true /f:text /c:10',
#     'wevtutil qe Application /q:"*[System[TimeCreated[timediff(@SystemTime) <= 86400000]]]" /rd:true /f:text /c:10'
# ]

# for command in commands:
#     print(f"Exécution de la commande : {command}")
#     output, error = run_command(command)
    
#     if error:
#         print(f"Erreur lors de l'exécution de la commande : {error}")
#     else:
#         print(f"Résultat de la commande :\n{output}")
#     print("----------------------------------")

# from xml.dom import minidom
# doc = minidom.parse('resultat.xml')
# print
# elem = doc.getElementsByTagName("Schannel")
# print(elem)
# time_created = doc.find('.//TimeCreated').attrib['SystemTime']
# source_name = doc.find('.//Provider').attrib['Name']
# description = doc.find('.//Message').text
# print(f"Date/heure : {time_created}")
# print(f"Source : {source_name}")
# print(f"Description : {description}")
# print("----------------------")

def ajouter_mot_fichier_xml(nom_fichier, motP,motD):
    # Lecture du fichier XML
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

    # Ajout du mot à la première et à la dernière ligne
    lignes[0] = motP + '' + lignes[0].strip() + '\n'
    lignes[-1] = lignes[-1].strip() + ' ' + motD + '\n'
    # Écriture du fichier modifié
    with open(nom_fichier, 'w') as fichier:
        fichier.writelines(lignes)

# Exemple d'utilisation
nom_fichier = 'resultat2.xml'
motP = '<Events>'
motD = '</Events>'

ajouter_mot_fichier_xml(nom_fichier, motP,motD)

from bs4 import BeautifulSoup

with open('resultat2.xml', 'r') as f:
    data = f.read()

# Parser le XML avec BeautifulSoup
soup = BeautifulSoup(data, 'xml')
events = soup.find_all('Event')
# print(events)
for event in events:
    try:
        if event is not None:
            system = event.find('System')
            provider_name = system.find('Provider')['Name']
            event_id = system.find('EventID').text
            time_created = system.find('TimeCreated')['SystemTime']
            event_record_id = system.find('EventRecordID').text
            data_typ = event.find('Data', {'Name': 'Type'})
            if data_typ is not None:
                data_type =data_typ.text
            else:
                print('Skip ...')
            error_stat = event.find('Data', {'Name': 'ErrorState'})
            if error_stat is not None:
                error_state=error_stat.text
            else:
                print('Skip ...')
        else:
            print("Le choix n'a pas été trouvé. Skip...")
        
        print('Provider Name:', provider_name)
        print('Event ID:', event_id)
        print('Time Created:', time_created)
        print('Event Record ID:', event_record_id)
        print('Data Type:', data_type)
        print('Error State:', error_state)
        print('---')
    except KeyboardInterrupt:
        print("\nEnregistrement des coordonnées terminé.")






