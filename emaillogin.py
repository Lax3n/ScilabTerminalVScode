import imaplib
from bs4 import BeautifulSoup

# Configuration
username = 'alexandre.sage41@gmail.com'
password = 'hhcy kbdr zcfx eiro'  # Utilisez un mot de passe d'application si nécessaire
imap_url = 'imap.gmail.com'
expediteur = "no-reply@opentable.com"

# Connexion au serveur IMAP
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(username, password)

mail.select("inbox")

# Recherche d'emails d'un expéditeur spécifique
status, messages = mail.search(None, '(FROM "{}")'.format(expediteur))

if status == 'OK':
    # Conversion du résultat de recherche en une liste d'identifiants d'email et récupération du dernier
    messages = messages[0].split(b' ')
    latest_email_id = messages[-1]

    # Récupération du dernier email
    status, data = mail.fetch(latest_email_id, '(RFC822)')
    # print(data)
    soup=BeautifulSoup(str(data),'html.parser')
    nombre = soup.find('span', {'id': '3D"copy-code"'})
    print(nombre.text)

    
else:
    print("Aucun message trouvé de cet expéditeur.")

# Déconnexion
mail.close()
mail.logout()