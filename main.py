import tls_client
import uuid
import imaplib
from bs4 import BeautifulSoup
import time
import json
import re

uuidcorrelationid = uuid.uuid4()
Xcsrftoken = uuid.uuid4()


session = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)
username = 'alexandre.sage41@gmail.com'
password = 'hhcy kbdr zcfx eiro'
imap_url = 'imap.gmail.com'
expediteur = "no-reply@opentable.com"

mail = imaplib.IMAP4_SSL(imap_url)
mail.login(username, password)

def login():
    Xcsrftokenlocal = uuid.uuid4()
    correlationid=uuid.uuid4()
    
    
    session.headers = {
        "authority": "www.opentable.com", 
        "path": "/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7",
        "Cache-Control":"no-cache",
        "Content-Type":"application/json",
        "Origin":"https://www.opentable.com",
        "Ot-Page-Group": "user",
        "Ot-Page-Type": "authentication_start",
        "Pragma":"no-cache",
        "Referer":"https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_heade",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "X-Csrf-Token": f"{Xcsrftokenlocal}",
        "X-Query-Timeout":"2000"
    }
    
    
    payloademail = {"operationName":"SendVerificationCodeEmail",
                    "variables":
                        {"verifyEmail":False,
                         "email":"alexandre.sage41@gmail.com",
                         "loginType":"popup-redirect",
                         "requestedAction":"https://www.opentable.com/",
                         "path":"https://www.opentable.com/authenticate/start?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_heade",
                         "origin":"unknown"},
                        "extensions":
                            {"persistedQuery":
                                {"version":1,
                                 "sha256Hash":"7a9ab940a239a8972a6157ace71d6885112aebf46d36592feaa828313a0eda21"}}}

    
    responsesendemail = session.post("https://www.opentable.com/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",json=payloademail)
    print(responsesendemail)
    code=mailcode()
    
    payloadlogin={"email":"alexandre.sage41@gmail.com",
                  "correlationId":f"{correlationid}",
                  "verificationCode":f"{code}",
                  "loginContextToken": '{\"loginType\":\"popup-redirect\",\"requestedAction\":\"https://www.opentable.com/\"}',
                  "recaptchaToken":"03AFcWeA55e4hx0CLDecBnsuYMD1fyUA-Pcjjx3ncrYrA9Dq3HBldA7HgQmcrh3_jfTHEaDRlaQPWeqd4jS5UhOGmBvR-TY0pn3fG9-5ZASvCHhE4ADOo5OoRb-P2Q2k3LpymzwHGK0-cR_TF57KzN7YpO_sHz1lZ9YoYK7SYuza-DsL9tBYkcysP_7RlpFLlzxjjmOUeTPqcdw4bNZGAxIkcwCOkgY1NJsvbUTJ7uF52FOhkvJsklTzPJwzuRwQGo_vE5mdTG2i6Yd7rHvmsi7dVRF7H-rbW8_evoVh2wEfAFg26qhqltAW0bfqV_Z38-nXi3b-_gAra01lpdDJjYTRL6n9VsxA1IHZjdsKODHPhwa_LlSGcRu006QqxqgwhyfxQqHBUSjBePzyGuntnWlWdKYMZoh1skRWRZaDU6150LXbqfHvYdNXyEP6JGTZRRolLRfvdrBxGBpei3rwMk9kUd7nhC50brN5yxFjETV1uATDu4sHEuGJ87M_yCGmxXjIm-kadRzpy4vSUTEKC1L7t9D6-1zkMp6EIwbqqemy1KVtn3Y6izj3MENc80dK9TC3b3iBFag6z5YxAXp9dVaTHN3inpTN1Y4W7Xroj8gs4q4WqiV1FB-c3ffbS15e7L63aEhirKaQVU6zGEJQPDswBRXu3GwPN9kIGv0irdyFRf1MPIzjc7it0uEK8ysqkSWmhLe4Kgn-H0d62ufsqXevBQt-4WllxYEZ9gKeL5C37PZm8J_2HDJRV2TWskAZbIZuky1n9lUrQDN7XsA5S-oF7tAEKIWDBFqJGCco6nGPMUcXderASqlTSnFZnvzojJZYgwwvY8rhonPIUeWbQtFacVNKtyf9gdO-ocYFoS8H3eDRmaFUO-Do2OqYjeErKmF1w4VX1Y8_UVlnvryG97eZI3G3SJ6v0T5q1HZa0HPzNCS1QQhcvxB7d9rtW4VXjfWB8TofWyGJaJZ96qjDeajL7AaaklhkPrf8va3TJs-_VXZcH5E_Agl-cIkO9v1AklLwY-qg5sxhj_rox_p357rnS3cgQXQTCIJtAzH0ep1LE_Nu7sjtsQQt_lyOMVEGSVZgq0ikCdmAJHvKWDVG1QzaRetK3dDFt398ofIA0ljwn3s5BB8W_M38eYBBQzshJDFYXgGabKOkhDWADITpcpD6UumHqzxHpQLW4YBtGXwA2DRtQb3cTtvHoj67bBsXCIiVo1YBjNwmLqeeV5J4qeYb83_X3oaKNUWsad_5wcxImtowcgLnfzJRWw-oCu-ntTKbJrAez0ISRPvY_V0q6TrOoCK2_3-_5bb3NW3c5rOvkIwvutoS0_dOPfeX2i9_gwBW5mKhwYQCGtUBubQK6Use7xGrbqrulNu3IatlIGqh8XAL2RNW2fZhHMNxfkjh1q8bCFg8zKX1Szwho6Y037uryvev6GhGmHCpgBaihVLIJYAmHyyKjWkFsc1walUwgN5PodiuRdfG-blWNztct1-YUlr7QueLA7Xrx0zvu1RgPS-DWtr2CJ2vMgF5me1nPGTgQlPU2D88XdIi826IFVEXDzVT3ydggE442DGeSnx-b3aX3_raTO74EODCiz3w37S7L03oK_k5_JcfVwTUSJLwJKYxp5jlhJ90ORLyUklxRgr0jyaTwrF5JEbHEPqWm46NZ_oD8Ngu5p-DUImctT5_3A3zpXyaPHfxodzppP-FlfLyMGK8jPTwZaOpQy6uSa6CrN-VjZOMdp",
                  "tld":"com",
                  "databaseRegion":"na",
                  "shouldEnableVerifyCredentials":True}
    
    responseconnexion=session.post("https://www.opentable.com/dapi/v1/authentication/start-passwordless-login",json=payloademail)
    print(responseconnexion)
    


def mailcode():
    

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
        spansoup = soup.find('span', {'id': '3D"copy-code"'})
        nombre=spansoup.text  
        print(nombre)
    else:
        print("Aucun message trouvé de cet expéditeur.")

    # Déconnexion
    mail.close()
    mail.logout()
    return nombre



def reservation(
    rid: int = 1268701,
    annee: str = "2024",
    mois: str = "03",
    jour: str = "10",
    heure: str = "21",
    minute: str = "15",
    nbperson: str = "2",
    nom: str = "Dupont",
    prenom: str = "Leo",
    email: str = "alexandre.sage41@gmail.com",
):

    session.headers = {
        "authority":"www.opentable.com",
        "path": "/",
        "scheme": "https",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Ot-Page-Group":"booking",
        "Ot-Page-Type":"network_detail",
        'Accept-Language' : 'fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7',
        "Content-Type":"application/json",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": 'empty',
        "Sec-Fetch-Mode": 'cors',
        "Sec-Fetch-Site": 'same-origin',
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "dnt":"1",
        "Referer":"https://www.opentable.com/",
        "Origin":"https://www.opentable.com/"
        
    }
    
    
    

    starturl = f"https://www.opentable.com/"
    responseSlotHash = session.execute_request("GET", starturl)
    print(responseSlotHash.status_code)
    # print(responseSlotHash.text)
    # soup=BeautifulSoup(responseSlotHash.text,"html.parser")
    # scripts=soup.find_all("script")
    # for script in scripts:
    #     if script.string:  # Vérifier si le script contient du texte
    #         slothash = re.findall(r'"slotHash":\s*"(\d+)"', script.string)
    #         print(slothash.group(1))
    
    session.headers.update({
       "x-csrf-token": f"{uuid.uuid4()}",
       "ot-page-type": "multi-search",
       "ot-page-group": "search"
    #    "referer": "https://www.opentable.com/s?dateTime=2024-03-29T21%3A00%3A00&covers=2&latitude=43.7045&longitude=7.2597&term=bad%20roman&shouldUseLatLongSearch=true&originCorrelationId=278b167c-97f0-4da1-a32d-cd6ceb705d4e&corrid=ccd0dc44-a8f9-4bed-908d-d90fc75ed6d0&intentModifiedTerm=bad%20roman&metroId=3534&originalTerm=bad%20roman&pinnedRid=1268701&queryUnderstandingType=default&sortBy=web_conversion"
    })
    
    payloadslothash={
	"operationName": "RestaurantsAvailability",
	"variables": {
		"onlyPop": False,
		"forwardDays": 0,
		"requireTimes": False,
		"requireTypes": [],
		"restaurantIds": [rid],
		"date": f"{annee}-{mois}-{jour}",
		"time": f"{heure}:{minute}",
		"partySize": nbperson,
		"databaseRegion": "NA",
		"restaurantAvailabilityTokens": ["eyJ2IjoyLCJtIjowLCJwIjowLCJzIjowLCJuIjowfQ"],
		"slotDiscovery": ["on"],
		"loyaltyRedemptionTiers": [],
		"attributionToken": "x=2024-03-05T21%3A13%3A30&c=1&pt1=1&pt2=1&er=0"
	},
	"extensions": {
		"persistedQuery": {
			"version": 1,
			"sha256Hash": "2aee2372b4496d091f057a6004c6d79fbf01ffdc8faf13d3887703a1ba45a3b8"
		}
	}
}
    
    responseslothash=session.post("https://www.opentable.com/dapi/fe/gql?optype=query&opname=RestaurantsAvailability",json=payloadslothash)
    print(responseslothash)
    # slothash = responseSlotHash.text.split('"slotHash"')[1].split('"')[1]
    # attributiontoken = responseSlotHash.text.split('"attributionToken"')[1].split('"')[1]

    
    # attributiontoken = responseSlotHash.text.split('"attributionToken"')[1].split('"')[1]
    # csrftoken = responseSlotHash.text.split("__CSRF_TOKEN__")[1].split("'")[1]

    session.headers.update({"X-Csrf-Token": f"{csrftoken}"})

    payloadreservation = {
        "additionalServiceFees": [],
        "attributionToken": f"{attributiontoken}",
        "correlationId": f"{uuidcorrelationid}",
        "country": "US",
        "diningAreaId": 1,
        "email": f"{email}",
        "firstName": f"{prenom}",
        "isModify": False,
        "dinerIsAccountHolder":False,
        "katakanaFirstName": "",
        "katakanaLastName": "",
        "lastName": f"{nom}",
        "nonBookableExperiences": [],
        "optInEmailRestaurant": False,
        "partySize": int(nbperson),
        "phoneNumber": "638054871",
        "phoneNumberCountryId": "FR",
        "points": 100,
        "pointsType": "Standard",
        "reservationAttribute": "default",
        "reservationDateTime": f"{annee}-{mois}-{jour}T{heure}:{minute}",
        "reservationType": "Standard",
        "restaurantId": rid,
        "slotAvailabilityToken": "eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ",
        # "slotHash": f"{slothash}",
        "tipAmount": 0,
        "tipPercent": 0,
    }
    # session.headers.update({"path":"/dapi/booking/make-reservation"})

    response = session.post("https://www.opentable.com/dapi/booking/make-reservation",json=payloadreservation)
    print(response.status_code)


# login()

jour = ["30", "29"]
heure = ["19"]
minute = ["00", "15", "30", "45"]
email = []

# reservation()

reservation(jour="23",heure="10",minute="30")
# reservation(jour="23",heure="20",minute="30",prenom="benard",nom="mazzeau")


# for i in range(len(jour)):
#     for j in range(len(heure)):
#         for k in range(len(minute)):
