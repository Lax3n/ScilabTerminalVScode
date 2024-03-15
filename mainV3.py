import tls_client
import uuid
import imaplib
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
import datetime
import os
import pickle
import json
import time
import threading





def mailcode()->int:
    time.sleep(5) #attente mail
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(username, password)
    mail.select("inbox")
    status, messages = mail.search(None, '(FROM "{}")'.format(expediteur))
    if status == 'OK':
        messages = messages[0].split(b' ')
        latest_email_id = messages[-1]
        status, data = mail.fetch(latest_email_id, '(RFC822)')
        # print(data)
        soup=BeautifulSoup(str(data),'html.parser')
        spansoup = soup.find('span', {'id': '3D"copy-code"'})
        nombre=spansoup.text  
    else:
        print("Aucun message trouvé de cet expéditeur.")
    mail.close()
    mail.logout()
    return nombre


def solvercaptcha():
    lien="https://www.opentable.fr/authenticate/start?rp=https%3A%2F%2Fwww.opentable.fr%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header"
    responsecaptcha=session.get(lien)
    key=responsecaptcha.text.split("?render=")[1].split("&")[0]
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


def reservationlogin(session,rid: int = 1268701,jour="05",mois="04",annee="2024",heure="20",minute="00",prenom="tata",nom="renault",nbpersonne=2,):
    
    global newsession
    correlationid=uuid.uuid4()
 
    # print(vars(session))
    # cookies=session.cookies
    # session.cookies=dict()
    url=f"https://www.opentable.fr/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&correlationId={correlationid}&creditCardRequired=false&dateTime=2024-{mois}-{jour}T{heure}%3A{minute}%3A00&partySize={nbpersonne}&points=100&pointsType=Standard&resoAttribute=default&rid={rid}&isModify=false&isMandatory=false&cfe=true"
    print(url)
    reponsextoken=newsession.get(url)
    print(reponsextoken)
    # print(reponsextoken.text)
    # session.cookies=cookies
    xtokenlocal=reponsextoken.text.split("__CSRF_TOKEN__='")[1].split("'")[0]
    slothash=reponsextoken.text.split('"slotHash"')[1].split('"')[1]
    # try:
    #     # print(reponsextoken.text)
    #     gpid=reponsextoken.text.split('"gpid":')[1].split(',')[0]
    # except IndexError:
    #     try:
    #         # securitytoken=reponsextoken.text.split('Token":"')[1].split('"')[0]
    #         # print(reponsextoken.text)
    #         # corfimationbumber=int(reponsextoken.text.split('onNumber":')[1].split(',')[0])
    #         session.headers.update({
    #     # 'Host': 'www.opentable.fr',
    #     'Connection': 'keep-alive',
    #     'Content-Length': '221',
    #     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    #     'ot-page-type': 'multi-search',
    #     'x-csrf-token': f'{xtokenlocal}',
    #     'sec-ch-ua-mobile': '?0',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    #     'content-type': 'application/json',
    #     'accept': '*/*',
    #     'x-query-timeout': '4014',
    #     'ot-page-group': 'search',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'Sec-GPC': '1',
    #     'Accept-Language': 'fr-FR,fr;q=0.7',
    #     'Origin': 'https://www.opentable.fr',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Referer': 'https://www.opentable.fr/s?dateTime=2024-04-06T19%3A00%3A00&covers=2&latitude=43.7045&longitude=7.2597&term=bad%20roman&shouldUseLatLongSearch=true&originCorrelationId=280a0fb0-f35c-489c-a6dc-91f69e055aa6&corrid=fc973cc3-21ef-4501-8afe-7bbfbcbb6242&intentModifiedTerm=bad%20roman&metroId=3534&originalTerm=bad%20roman&pinnedRid=1268701&queryUnderstandingType=default&sortBy=web_conversion',
    #     'Accept-Encoding': 'gzip, deflate, br'
    # })
            
            
            
    #         payloadgpib={
    #     "operationName": "HeaderUserProfile",
    #     "variables": {
    #         "isAuthenticated": False,
    #         "tld": "fr",
    #         "gpid": 0
    #     },
    #     "extensions": {
    #         "persistedQuery": {
    #             "version": 1,
    #             "sha256Hash": "5de3544592811db1a5a2dae7acfd191b958d0aca8d773a2a2fc056c04e90b216"
    #         }
    #     }
    # }
            
    #         reponsegpid=session.post("https://www.opentable.fr/dapi/fe/gql?optype=query&opname=HeaderUserProfile",json=payloadgpib)
    #         gpid=reponsegpid.text.split('"gpid":')[1].split(',')[0]
    #     except:
    #         pass
                # print(slothash)
    # print(gpid)
    # print(xtokenlocal)
    payloadslotlockid={
        "operationName": "BookDetailsStandardSlotLock",
        "variables": {
            "slotLockInput": {
                "restaurantId": rid,
                "seatingOption": "DEFAULT",
                "reservationDateTime": f"{annee}-{mois}-{jour}T{heure}:{minute}",
                "partySize": nbpersonne,
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
    formatted_now = now.strftime("%Y-%m-%dT%H:%M:%S").replace(":", "%3A")

    session.headers.update({
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',       
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
        'Referer': f'https://www.opentable.fr/booking/details?availabilityToken=eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ&correlationId=d376c484-53b9-4da2-bc14-4d8371d170e5&creditCardRequired=false&dateTime=2024-03-17T22%3A00%3A00&partySize=2&points=100&pointsType=Standard&resoAttribute=default&rid={rid}&slotHash={slothash}&isModify=false&isMandatory=false&cfe=true',
        'Accept-Encoding': 'gzip, deflate, br'
    })


    payloadreservation={
        "restaurantId": rid,
        "slotAvailabilityToken": "eyJ2IjoyLCJtIjowLCJwIjowLCJjIjo2LCJzIjowLCJuIjowfQ",
        "slotHash": f"{slothash}",
        "slotLockId": slotlockid,
        "isModify": False,
        "nonBookableExperiences": [],
        "reservationDateTime": f"{annee}-{mois}-{jour}T{heure}:{minute}",
        "partySize": nbpersonne,
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


def startsession():
    global session
    if os.path.exists("./cache/cookies.pickle") and os.path.exists("./cache/headers.json"):
        with open("./cache/cookies.pickle","rb") as f:
            print("je passe par ici")
            session.cookies=pickle.load(f)
        with open("./cache/headers.json","rb") as f:
            session.headers.update(json.load(f))

    else:
        session=login(session=session)
        with open("./cache/cookies.pickle","wb") as f:
            pickle.dump(session.cookies,f)  
        headers = session.headers
        headers_bytes = {k: str(v) for k, v in headers.items()}
        with open('./cache/headers.json', 'w', encoding='utf-8') as f:
            json.dump(headers_bytes, f, indent=4)
    
    # return session
        
def iteration(session):
    names=[('Grace', 'Wilson'), ('Rachel', 'Walker'), ('Larry', 'King'), ('Xavier', 'Smith'), ('Olivia', 'Lee'), ('Dave', 'Hernandez'), ('Ida', 'Rodriguez'), ('Quinn', 'Wright'), ('Carol', 'Allen'), ('Peter', 'Clark'), ('Bob', 'Hall'), ('Frank', 'Thomas'), ('Tony', 'Martin'), ('Mary', 'Moore'), ('Sam', 'Harris'), ('Eve', 'Garcia'), ('Henry', 'Lewis'), ('Nick', 'Thompson'), ('Jack', 'Scott'), ('Victor', 'Taylor'), ('Wendy', 'Anderson'), ('Alice', 'Thompson'), ('Kate', 'Young'), ('Uma', 'Martinez'), ('Zoe', 'Harris')]
    heure=["19"]
    minutes=["00","15","30","45","00","15","30","45"]
    nombre=[2,4,5,6,2,4,2,6]
    threads = []
    for eachthread in range(8):
        thread=threading.Thread(target=reservationlogin, args=(session,1268701,"05","04","2024","19",minutes[eachthread],names[eachthread][0],names[eachthread][1],nombre[eachthread]))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        
    

    
    
        
    
    
    
    
    
if __name__=="__main__":
    
    uuidcorrelationid = uuid.uuid4()
    Xcsrftoken = uuid.uuid4()
    session = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)
    newsession = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)
    username = 'alexandre.sage41@gmail.com'
    password = os.environ["GoogleApplication"]
    imap_url = 'imap.gmail.com'
    expediteur = "no-reply@opentable.com"
    apikey=os.environ["TwoCaptchaAPI"]
    solver = TwoCaptcha(apikey)
    startsession()
    # iteration(session=sessionprete)
    reservationlogin(session)
    
    

    
            
        