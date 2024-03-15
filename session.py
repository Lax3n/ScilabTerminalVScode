import requests
import fake_useragent
import json

# Créer un objet UserAgent et un objet Session
ua = fake_useragent.UserAgent()
session = requests.session()

# Effectuer une requête GET pour obtenir le hash SHA256
url_sha256 = "https://cdn.otstatic.com/cfe/14/js/home-K6ITR4D6.js"
response_get = session.get(url_sha256, headers={"Content-Type": "application/json"})
print(response_get.status_code)

# Extraire le hash SHA256 du texte de la réponse
sha256 = response_get.text.split("documentId")[1].split('"')[1]

# Mettre à jour le payload avec le hash SHA256 extrait
payload = {
    "operationName": "HomeModuleLists",
    "extensions": {
        "persistedQuery": {
            "sha256Hash": sha256,  # Utiliser le hash SHA256 extrait ici
            "version": 1
        }
    }
}

# Effectuer une requête GET pour la page principale avec l'objet Session
url_main = "https://www.opentable.fr/"
response = session.get(url_main, headers={"User-Agent": ua.random})
print(response.status_code)

url_main = "https://www.opentable.fr/r/bad-roman-new-york?corrid=b85d427b-9b55-4369-9457-811fe5849601&avt=eyJ2IjoyLCJtIjowLCJwIjowLCJzIjowLCJuIjowfQ&p=2&sd=2024-03-02T12%3A00%3A00"
response = session.get(url_main, headers={"User-Agent": ua.random})
print(response.status_code)

# Mettre à jour le payload de la requête POST avec les données requises (actuellement vide)
# payload_corrid = {...}

# Effectuer une requête POST avec l'objet Session et mettre à jour les en-têtes et les données
url_corrid = "https://www.opentable.fr/dapi/fe/gql?optype=query&opname=Autocomplete"
response_corrid = session.post(url_corrid, json=payload, headers={
    "User-Agent": ua.random # Utiliser les cookies de la session au lieu de les définir manuellement
})
print(response_corrid.status_code)
