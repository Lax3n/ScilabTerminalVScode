import requests
import time


reponse=requests.get("https://www.opentable.fr/") #2024(année)-03(mois)-02(jour)T12(heure)%3A00(minute)%3A00(seconde?)
print(reponse.content)