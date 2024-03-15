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


uuidcorrelationid = uuid.uuid4()
Xcsrftoken = uuid.uuid4()
session = tls_client.Session(client_identifier="chrome_120",)
# newsession = tls_client.Session(client_identifier="chrome_117", random_tls_extension_order=True)
username = 'alexandre.sage41@gmail.com'
password = os.environ["GoogleApplication"]
imap_url = 'imap.gmail.com'
expediteur = "no-reply@opentable.com"
apikey=os.environ["TwoCaptchaAPI"]
solver = TwoCaptcha(apikey)





def login(session):
    # global Xcsrftokenlocal
    Xcsrftokenlocal = uuid.uuid4()
    correlationid=uuid.uuid4()
    
    
    session.headers = {
        # "authority": "www.opentable.com", 
        # "path": "/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",
        # "scheme": "https",
        "connection":"keep-alive",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7",
        "Cache-Control":"no-cache",
        "Content-Type":"application/json",
        "Origin":"https://www.opentable.com",
        "Ot-Page-Group": "user",
        "Ot-Page-Type": "authentication_start",
        # "Pragma":"no-cache",
        "Referer":"https://www.opentable.com/authenticate/verify-medium?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&iscomomBookingFlow=false&isPopup=true&origin=global_header",
        "Sec-Ch-Ua": '"Chromium";v="117", "Not(A:Brand";v="24", "Google Chrome";v="117',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        "x-csrf-token": f"{Xcsrftokenlocal}",
        "X-Query-Timeout":"2000"  
    }
    session.get("https://www.opentable.com/")
    response=session.get("https://www.opentable.com/authenticate/start?rp=https://www.opentable.com/&srs=1&iscomomBookingFlow=false&isPopup=true&origin=global_header")
    print(response)
    
    try:
        xsrftoken=response.text.split("__CSRF_TOKEN__='")[1].split("'")[0]
        session.headers.update({
            "x-csrf-token":xsrftoken
        })
        # print(f'"{xsrftoken}"')
    except:
        print("marche pas")
    # print(response)
    # print(response)
    
    
    payloademail = {
	"operationName": "SendVerificationCodeEmail",
	"variables": {
		"verifyEmail": False,
		"email": "alexandre.sage41@gmail.com",
		"loginType": "popup-redirect",
		"requestedAction": "https://www.opentable.com/",
		"path": "https://www.opentable.com/",
		"origin": "global_header"
	},
	"extensions": {
		"persistedQuery": {
			"version": 1,
			"sha256Hash": "7a9ab940a239a8972a6157ace71d6885112aebf46d36592feaa828313a0eda21"
		}
	}
}
    
    payloadmix1={
	"event": "page_view_home",
	"meta": {
		"cookies_enabled": True,
		"hostname": "https://www.opentable.com",
		"path": "/",
		"search": "",
		"title": "Restaurants and Restaurant Reservations | OpenTable",
		"referrer": "",
		"page_group": "seo-landing-home",
		"page_type": "home",
		"is_page_view": True
	}
}
    
    responsemix1=session.post("https://www.opentable.com/dapi/v1/mix",json=payloadmix1)
    print(responsemix1)

    
    responsesendemail = session.post("https://www.opentable.com/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",json=payloademail)
    print(responsesendemail)
    print(responsesendemail.text)
    
    payloadmix2={
	"event": "page_view_authentication_verify_medium",
	"meta": {
		"cookies_enabled": True,
		"hostname": "https://www.opentable.com",
		"path": "/verify-medium",
		"search": "?rp=https://www.opentable.com/&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header",
		"title": "Log In / Sign Up",
		"referrer": "https://www.opentable.com/",
		"page_group": "user",
		"page_type": "authentication_verify_medium",
		"is_page_view": True
	}
}
    
    responsemix2=session.post("https://www.opentable.com/dapi/v1/mix",json=payloadmix2)
    print(responsemix2)
    
    
    
    # print(responsesendemail.text)
    correlationid=str(responsesendemail.text.split('"correlationId":"')[1].split('"')[0])
    # print(f'"{correlationid}"')
    code=mailcode()
    print(f"{code}")
    recaptchatoken=solvercaptcha()
    # print(recaptchatoken)
    
    payloadlog=["info", {
	"pageGroup": "user",
	"preloadJsBundles": [],
	"pageType": "authentication_verify_medium",
	"countryIp": "FR",
	"cityIp": "UNKNOWN",
	"rateLimit": 3,
	"concurrentRequests": 1,
	"message": "recaptcha",
	"sub-message": "recaptcha executed in 438 total 438",
	"related-url": "https://www.opentable.com/authenticate/verify-medium?rp=https://www.opentable.com/&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header",
	"header-user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
	"header-referer": "https://www.opentable.com/"
}]
    
    
    responselog=session.post("https://www.opentable.com/dapi/fe/log",json=payloadlog)
    print(responselog)
    
    
    payloadreport={
	"meta": {
		"navigationStart": 1710232139548,
		"pageType": "home",
		"usersCity": "UNKNOWN",
		"pageGroup": "seo-landing-home",
		"deviceType": "desktop",
		"primaryCountry": "us",
		"metroId": "undefined",
		"clientLoaded": True,
		"reportTime": 1710232159323
	},
	"metrics": {
		"scriptWeight": 0,
		"imgWeight": 2418,
		"FCP": 2580,
		"LCP": 5147,
		"TTFB": 1945,
		"CLS": 51,
		"INP": 120,
		"FID": 1
	}
}
    
    
    responsereport=session.post("https://www.opentable.com/dapi/fe/proxy/consumer-frontend/rum-report",json=payloadreport)
    print(responsereport)
    
    
    
    # # print(payload)
    # session.headers.update({
    #     # "authority": "www.opentable.com", 
    #     # "path": "/dapi/fe/gql?optype=mutation&opname=SendVerificationCodeEmail",
    #     # "scheme": "https",
    #     "Accept": "application/json",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "fr-FR,fr;q=0.9, en-US; q=0.8, en; q=0.7",
    #     # "Cache-Control":"no-cache",
    #     "Content-Type":"application/json",
    #     "Origin":"https://www.opentable.com",
    #     # "Ot-Page-Group": "user",
    #     # "Ot-Page-Type": "authentication_start",
    #     "Pragma":"no-cache",
    #     "Referer":"https://www.opentable.com/authenticate/verify-medium?rp=https%3A%2F%2Fwww.opentable.com%2F&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header",
    #     "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    #     "Sec-Ch-Ua-Mobile": "?0",
    #     "Sec-Ch-Ua-Platform": '"Windows"',
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-origin",
    #     "Sec-Gpc": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    #     # "x-csrf-token": f"{Xcsrftokenlocal}",
    #     # "X-Query-Timeout":"2000"
    # })
    payloadlogin={
	"email": f"{username}",
	"correlationId": f"{correlationid}",
	"verificationCode": f"{code}",
	"loginContextToken":"{\"loginType\":\"popup-redirect\",\"requestedAction\":\"https://www.opentable.com/\"}",
	"recaptchaToken": f"{recaptchatoken}",
	"tld": "com",
	"databaseRegion": "na",
	"shouldEnableVerifyCredentials": True,
    # "keys":["verificationCode"]
 
    }
    
    session.headers={
    "path": "/dapi/v1/authentication/start-passwordless-login",
    # "content-length": "2297",
    "sec-ch-ua": '"Chromium";v="120", "Not(A:Brand";v="24", "Brave";v="120"',
    "accept": "application/json",
    "content-type": "application/json",
    "x-csrf-token": f"{xsrftoken}",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": '"Windows"',
    "sec-gpc": "1",
    "accept-language": "fr-FR,fr;q=0.8",
    "origin": "https://www.opentable.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.opentable.com/authenticate/verify-medium?rp=https://www.opentable.com/&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header",
    "accept-encoding": "gzip, deflate, br"
}
    
    
    # print(payloadlogin)
    print(session.headers)
    
    
    
    responselogin=session.post("https://www.opentable.com/dapi/v1/authentication/start-passwordless-login",json=payloadlogin)
    print(responselogin)
    # print(session.cookies)
    print(responselogin.text)
    return session


def mailcode():
    time.sleep(10) #attente mail
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
    lien="https://www.opentable.com/authenticate/start?rp=https://www.opentable.com/&srs=1&isFromBookingFlow=false&isPopup=true&origin=global_header"
    responsecaptcha=session.get(lien)
    key=responsecaptcha.text.split("?render=")[1].split("&")[0]
    try:
        result = solver.solve_captcha(f'{key}',f'{lien}')
        return result
    except:
        print("error captcha")


login(session)