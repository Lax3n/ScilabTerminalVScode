import tls_client
import uuid
import imaplib
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
import sys
import datetime
import os
import pickle
import json
import time





def mailcode()->int:
    time.sleep(5)
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
        spansoup = soup.find('span', {'id': '3D"copy-code"'})
        nombre=spansoup.text  
        # print(nombre)
    else:
        print("Aucun message trouvé de cet expéditeur.")
    # Déconnexion
    mail.close()
    mail.logout()
    return nombre


def solvercaptcha():
    lien="https://www.opentable.fr/authenticate/start?rp=https%3A%2F%2Fwww.opentable.fr%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header"
    responsecaptcha=session.get(lien)
    # print(responsecaptcha.status_code)
    key=responsecaptcha.text.split("?render=")[1].split("&")[0]
    # print(key)
    # try:
    result = solver.solve_captcha(f'{key}',f'{lien}')
    return result


def login(session):
    # global Xcsrftokenlocal
    Xcsrftokenlocal = uuid.uuid4()
    correlationid=uuid.uuid4()
    
    
    session.headers = {
        # "authority": "www.opentable.com", 
        # "path": "/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",
        # "scheme": "https",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7",
        # "Cache-Control":"no-cache",
        "Content-Type":"application/json",
        "Origin":"https://www.opentable.com",
        # "Ot-Page-Group": "user",
        # "Ot-Page-Type": "authentication_start",
        "Pragma":"no-cache",
        "Referer":"https://www.opentable.com/authenticate/verify-medium?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "x-csrf-token": f"{Xcsrftokenlocal}",
        # "X-Query-Timeout":"2000"
    }
    response=session.get("https://www.opentable.com/")
    # print(response)
    
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
    recaptchatoken=solvercaptcha()
    # print(recaptchatoken)
    payload={
	"email": "alexandre.sage41@gmail.com",
	"correlationId": f"{correlationid}",
	"verificationCode": code,
	"loginContextToken": "{\"loginType\":\"popup-redirect\",\"requestedAction\":\"https://www.opentable.com/\"}",
	"recaptchaToken": f"{recaptchatoken}",
	"tld": "com",
	"databaseRegion": "na",
	"shouldEnableVerifyCredentials": True
    }
    # print(payload)
    responselogin=session.post("https://www.opentable.com/dapi/v1/authentication/start-passwordless-login",json=payload)
    print(responselogin)
    return session


def reservationlogin(session,rid: int = 1268701,
                    jour="25",
                    mois="03",
                    annee="2024",
                    heure="22",
                    minute="15",
                    prenom="toto",
                    nom="renault",
):
    reponsextoken=session.get(f"https://www.opentable.fr/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&creditCardRequired=false&dateTime={annee}-{mois}-{jour}T{heure}%3A{minute}%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid=1268701&isModify=false&isMandatory=false&cfe=true")
    xtokenlocal=reponsextoken.text.split("__CSRF_TOKEN__='")[1].split("'")[0]
    slothash=reponsextoken.text.split('"slotHash"')[1].split('"')[1]
    gpid=reponsextoken.text.split('"gpid":')[1].split(',')[0]

    print(slothash)
    print(gpid)
    print(xtokenlocal)

    # time.sleep(10)
    # payloadgpid={
    # 	"operationName": "HeaderUserProfile",
    # 	"variables": {
    # 		"isAuthenticated": False,
    # 		"tld": "fr",
    # 		"gpid": 0
    # 	},
    # 	"extensions": {
    # 		"persistedQuery": {
    # 			"version": 1,
    # 			"sha256Hash": "5de3544592811db1a5a2dae7acfd191b958d0aca8d773a2a2fc056c04e90b216"
    # 		}
    # 	}
    # }


    # session.headers.update({
    # 	"x-csrf-token": f"{xtokenlocal}",
    # 	# "Host": "www.opentable.fr",
    #     # "Content-Length": "221",
    #     "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    #     "ot-page-type": "home",
    #     # "x-csrf-token": "436ef73d-585a-4fe8-bf19-ac56921214ba",
    #     "sec-ch-ua-mobile": "?0",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    #     "content-type": "application/json",
    #     "accept": "*/*",
    #     "x-query-timeout": "4014",
    #     "ot-page-group": "seo-landing-home",
    #     "sec-ch-ua-platform": '"Windows"',
    #     "Sec-GPC": "1",
    #     "Accept-Language": "fr-FR,fr;q=0.8",
    #     "Origin": "https://www.opentable.fr",
    #     "Sec-Fetch-Site": "same-origin",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Dest": "empty",
    #     "Referer": "https://www.opentable.fr/",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     # "Cookie": "otuvid=F95997F3-9029-4568-AC67-A4F8B936DF75; OT-SessionId=bf7986bd-2882-447e-960e-87c0597daae4; ha_userSession=lastModified=2024-02-22T12%3A59%3A05.000Z&origin=prod-rs; uCke=lo=DFyyr06XGtzc%2Bb6bGMZ%2FaWzNyHaPXHIF%2F%2FRZ%2ByE2y%2FI%3D&em=DFyyr06XGtzc%2Bb6bGMZ%2FaWzNyHaPXHIF%2F%2FRZ%2ByE2y%2FI%3D&gpid=KdlHFRC34MXLBJ%2BBJY8Z0A%3D%3D&gid=190209510679&l=1&t=1; authCke=atk=81d0e1ad-49b1-48d3-a7ad-57eec0d6f19b&rtk=90615d89-a2fa-4ace-8e68-20b47b9e161b&tks=CONSUMER&tkt=bearer&eik=949928&tcd=2024-03-08T21%3A08%3A48.631Z&atke=2024-03-19T21%3A00%3A56.631Z; OT-Session-Update-Date=1709932128; ftc=x=2024-03-08T22%3A08%3A48&c=1&pt1=1&pt2=1",
    #     "Connection": "keep-alive"
    # }
    # )



    # reponsegpid=session.post("https://www.opentable.fr/dapi/fe/gql?optype=query&opname=HeaderUserProfile",json=payloadgpid)
    # print(reponsegpid.text)
    # print(reponsegpid)
    # gpid=reponsegpid.text.split('"gpid":')[1].split(",")[0]
    # # print(gpid)

    # session.headers.update({
    #     # "Host": "www.opentable.fr",
    #     "Connection": "keep-alive",
    #     # "Content-Length": "548",
    #     "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    #     "ot-page-type": "multi-search",
    #     # "x-csrf-token": f"{xtokenlocal}",
    #     "sec-ch-ua-mobile": "?0",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    #     "content-type": "application/json",
    #     "accept": "*/*",
    #     "x-query-timeout": "5500",
    #     "ot-page-group": "search",
    #     "sec-ch-ua-platform": '"Windows"',
    #     "Sec-GPC": "1",
    #     "Accept-Language": "fr-FR,fr;q=0.8",
    #     "Origin": "https://www.opentable.fr",
    #     "Sec-Fetch-Site": "same-origin",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Dest": "empty",
    #     # "Referer": "https://www.opentable.fr/s?dateTime=2024-03-25T22%3A00%3A00&covers=2&latitude=43.7045&longitude=7.2597&term=bad%20roman&shouldUseLatLongSearch=true&originCorrelationId=9874734d-c820-4ee7-8a21-98a55d144f64&corrid=105ee830-dc3e-4cdd-9427-894bb52b5c7e&intentModifiedTerm=bad%20roman&metroId=3534&originalTerm=bad%20roman&pinnedRid=1268701&queryUnderstandingType=default&sortBy=web_conversion",
    #     "Accept-Encoding": "gzip, deflate, br"
    # })


    # payload={
    # 	"operationName": "RestaurantsAvailability",
    # 	"variables": {
    # 		"onlyPop": False,
    # 		"forwardDays": 0,
    # 		"requireTimes": False,
    # 		"requireTypes": [],
    # 		"restaurantIds": [1268701],
    # 		"date": f"{annee}-{mois}-{jour}",
    # 		"time": f"{heure}:{minute}",
    # 		"partySize": 2,
    # 		"databaseRegion": "EU",
    # 		"restaurantAvailabilityTokens": ["eyJ2IjoyLCJtIjowLCJwIjowLCJzIjowLCJuIjowfQ"],
    # 		"slotDiscovery": ["on"],
    # 		"loyaltyRedemptionTiers": [],
    # 		"attributionToken": f"x={formatted_now}&c=1&pt1=1&pt2=1&er=0"
    # 	},
    # 	"extensions": {
    # 		"persistedQuery": {
    # 			"version": 1,
    # 			"sha256Hash": "2aee2372b4496d091f057a6004c6d79fbf01ffdc8faf13d3887703a1ba45a3b8"
    # 		}
    # 	}
    # }

    # # reponseslothash=session.post("https://www.opentable.fr/dapi/fe/gql?optype=query&opname=RestaurantsAvailability")


    # reponse=session.post("https://www.opentable.fr/dapi/fe/gql?optype=query&opname=RestaurantsAvailability",json=payload)
    # slothash=str(int(reponse.text.split('"slotHash"')[1].split('"')[1])) #slotHHHHHHHHash avec un h majuscule
    # print(slothash)
    payloadslotlockid={
        "operationName": "BookDetailsStandardSlotLock",
        "variables": {
            "slotLockInput": {
                "restaurantId": 1268701,
                "seatingOption": "DEFAULT",
                "reservationDateTime": f"{annee}-{mois}-{jour}T{heure}:{minute}",
                "partySize": 2,
                "databaseRegion": "EU",
                "slotHash": f"{slothash}",
                "reservationType": "STANDARD",
                "diningAreaId": 1
            }
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "fb25981b6242087d3313d9f3cad196725c65694ef3ac681b842e55f382f3de90"
            }
        }
    }
    reponseslotlockid=session.post("https://www.opentable.fr/dapi/fe/gql?optype=mutation&opname=BookDetailsStandardSlotLock",json=payloadslotlockid)
    print(reponseslotlockid.text)
    slotlockid=int(reponseslotlockid.text.split('"slotLockId":')[1].split(',')[0])

    now = datetime.datetime.now()

    # Formatage de la date et l'heure actuelles
    formatted_now = now.strftime("%Y-%m-%dT%H:%M:%S").replace(":", "%3A")

    session.headers.update({
        # 'Host': 'www.opentable.fr',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '805',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        # 'x-csrf-token': f"{xtokenlocal}",
        
        'Accept-Language': 'fr-FR, fr, en, *',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-GPC': '1',
        'Origin': 'https://www.opentable.fr',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://www.opentable.fr/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&correlationId=d376c484-53b9-4da2-bc14-4d8371d170e5&creditCardRequired=false&dateTime=2024-03-17T22%3A00%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid=1268701&slotHash={slothash}&isModify=false&isMandatory=false&cfe=true',
        'Accept-Encoding': 'gzip, deflate, br'
    })


    payloadreservation={
        "restaurantId": 1268701,
        "slotAvailabilityToken": "eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ",
        "slotHash": f"{slothash}",
        "slotLockId": slotlockid,
        "isModify": False,
        "nonBookableExperiences": [],
        "reservationDateTime": f"{annee}-{mois}-{jour}T{heure}:{minute}",
        "partySize": 2,
        "firstName": prenom,
        "lastName": nom,
        "email": "alexandre.sage41@gmail.com",
        "dinerIsAccountHolder": False,
        "country": "US",
        "reservationType": "Standard",
        "reservationAttribute": "default",
        "katakanaFirstName": "",
        "katakanaLastName": "",
        "gpid": gpid,
        "correlationId": f"{uuid.uuid4()}",
        "attributionToken": f"x={formatted_now}&c=1&pt1=1&pt2=1&er=0",
        "additionalServiceFees": [],
        "tipAmount": 0,
        "tipPercent": 0,
        "pointsType": "None",
        "points": 0,
        "diningAreaId": 1,
        "phoneNumber": "638054871",
        "phoneNumberCountryId": "FR",
        "optInEmailRestaurant": False
    }

    reponseresa=session.post("https://www.opentable.fr/dapi/booking/make-reservation",json=payloadreservation)
    print(reponseresa)
    
    
if __name__=="__main__":
    
    uuidcorrelationid = uuid.uuid4()
    Xcsrftoken = uuid.uuid4()
    session = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)
    username = 'alexandre.sage41@gmail.com'
    password = os.environ["GoogleApplication"]
    imap_url = 'imap.gmail.com'
    expediteur = "no-reply@opentable.com"
    apikey=os.environ["TwoCaptchaAPI"]
    solver = TwoCaptcha(apikey)
    

    if os.path.exists("./cache/cookies.pickle") and os.path.exists("./cache/headers.json"):
        with open("./cache/cookies.pickle","rb") as f:
            print("je passe par ici")
            session.cookies=pickle.load(f)
        with open("./cache/headers.json","rb") as f:
            session.headers.update(json.load(f))
    
  
    else:
        sessionlogin=login(session=session)
        print(sessionlogin.headers)
        with open("./cache/cookies.pickle","wb") as f:
            pickle.dump(sessionlogin.cookies,f)  
        headers = sessionlogin.headers
        headers_bytes = {k: str(v) for k, v in headers.items()}
        with open('./cache/headers.json', 'w', encoding='utf-8') as f:
            json.dump(headers_bytes, f, indent=4)
            
        