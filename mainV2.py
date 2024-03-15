import tls_client
import uuid
import imaplib
from bs4 import BeautifulSoup
import os
from twocaptcha import TwoCaptcha
import sys
import time

uuidcorrelationid = uuid.uuid4()
Xcsrftoken = uuid.uuid4()



session = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)
username = 'alexandre.sage41@gmail.com'
password = os.environ["GoogleApplication"]
imap_url = 'imap.gmail.com'
expediteur = "no-reply@opentable.com"

apikey=os.environ["TwoCaptchaAPI"]
solver = TwoCaptcha(apikey)


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
        # pass

    # except Exception as e:
    #     sys.exit(e)


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
    # print(responselogin.text)

def reservationlogin(session,rid: int = 1268701):
    pass
    
    
    

# session=login(session)
    
# reservationlogin(session=session)
# print(recaptcha())