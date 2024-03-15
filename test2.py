import datetime

# Obtenir la date et l'heure actuelles
now = datetime.datetime.now()

# Formatage de la date et l'heure actuelles
formatted_now = now.strftime("%Y-%m-%dT%H:%M:%S").replace(":", "%3A")
print(formatted_now)